import sys
from iotbx import mtz
from cctbx.array_family import flex
import iotbx
import subprocess
import glob

#Read the 1st mtz file
mtz1 = mtz.object(sys.argv[1])

#Read the 2nd mtz file
mtz2 = mtz.object(sys.argv[2])

#Extract miller arrays by using cctbx
refl1_ = mtz1.as_miller_arrays()
refl2_ = mtz2.as_miller_arrays()


ref1 = [x for x in refl1_ if x.info().labels][0]
ref2 = [x for x in refl2_ if x.info().labels][0]

ref1=ref1.as_amplitude_array()
ref2=ref2.as_amplitude_array()

# Common reflections
com1,com2 = ref1.common_sets(ref2,assert_is_similar_symmetry=False)

## calculate cc
difff = flex.linear_correlation(com1.data()**2,com2.data()**2).coefficient()
result_list=[]
result_list.append(difff)

with open('over_test.txt','a')as f:
    for line in result_list:
        f.write(str(line))
        f.write("\n")

