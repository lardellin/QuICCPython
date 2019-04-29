import sys, os
env = os.environ.copy()
sys.path.append(env['HOME'] + '/workspace/QuICCPython/')
from scipy.io import savemat
from QuICCPython.read import SpectralState
from QuICCPython.shell.spectral import computeZIntegral, getMeridionalSlice,\
    getEquatorialSlice, getIsoradiusSlice, processState

# define the main process file
def main(filename):

    # open the state
    state = SpectralState(filename, 'shell')
    
    # turn the file in the frame of rotation and subtract unif vorticity'
    processedState = processState(state)    

    Ns = 3/E**.3
    spectralUS = computeZIntegral(processedState, 'uS', Ns)
    savemat('GeostrophicUS.mat', mdict = spectralUS)
    
    spectralUPhi = computeZIntegral(processedState, 'uPhi', Ns)
    savemat('GeostrophicUPhi.mat', mdict = spectralUPhi)
    
    spectralVortZ = computeZIntegral(processedState, 'vortZ', Ns)
    savemat('GeostrophicVortZ.mat', mdict = spectralVortZ)

    
    meridFields = getMeridionalSlice()
    savemat('MeridionalFlowPhys.mat', mdict = meridFields)
    equatFields = getEquatorialSlice()
    savemat('EquatorialFlowPhys.mat', mdict = equatFields)
    midFields = getIsoradiusSlice()
    savemat('MidradiusFlowPhys.mat', mdict = midFields)

    # output the fields in the boundary layers
    E = spectralVisualizer.parameters.ekman
    innerBound = getIsoradiusSlice(r = 2.* E **.5)
    savemat('IBoundaryFlowPhys.mat', mdict = innerBound)
    outerBound = getIsoradiusSlice(r = 1 - 2. * E**.5)
    savemat('OBoundaryFlowPhys.mat', mdict = outerBound)
                
    return
    
if __name__=="__main__":
    main(sys.argv[1])