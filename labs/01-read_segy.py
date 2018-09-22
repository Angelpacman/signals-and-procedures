#leer y escribir un segy y graficarlo

import numpy as np
import matplotlib.pyplot as plt


from obspy.io.segy.segy import _read_segy

stream = _read_segy('/home/angelr/Documentos/MIGRACION/su/tape01.segy', headonly=True)

one_trace = stream.traces[0]

plt.figure(figsize=(12,4))
plt.plot(one_trace.data)
plt.show()
data = np.stack(t.data for t in stream.traces)

print(data.shape)

vm = np.percentile(data, 99)

print("The 99th percentile is {:.0f}; the max amplitude is {:.0f}".format(vm, data.max()))
plt.figure(figsize=(8,8))
plt.imshow(data.T, cmap="Greys", vmin=-vm, vmax=vm, aspect='auto')


plt.figure(figsize=(10,6))
plt.imshow(data.T, cmap="RdBu", vmin=-vm, vmax=vm, aspect='auto')
plt.colorbar()
plt.show()
# If you get nonsense here, the header is probably EBCDIC encoded.
# In that case pass ``encoding='cp037'`` to ``decode``.
print(stream.textual_file_header.decode())
x = np.array(list(stream.textual_file_header.decode()))
print(stream.binary_file_header)
print(stream.traces[0].header)
plt.plot([t.header.trace_sequence_number_within_segy_file for t in stream.traces])
plt.show()



#escribiendo los datos
from obspy.core import AttribDict
from obspy.core import Stats

from obspy.core import Trace, Stream
from obspy.io.segy.segy import SEGYBinaryFileHeader
from obspy.io.segy.segy import SEGYTraceHeader

import bruges

dt = stream.traces[0].header.sample_interval_in_ms_for_this_trace / 1e6
similarity = bruges.attribute.similarity(data, duration=0.16, dt=dt)

plt.figure(figsize=(16,8))
plt.imshow(similarity.T, cmap="viridis", aspect='auto')
plt.colorbar()
plt.show()
