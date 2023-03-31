import argparse
import PyATEMMax

parser = argparse.ArgumentParser()
parser.add_argument('--ip', help='switcher IP address', type=str, default="10.0.0.202")
parser.add_argument('-m', '--mixeffect', help='select mix effect (0/1), default 0', type=int, default=0)
parser.add_argument('-i', '--input', help='Input to switch to', type=int, default=1)
args = parser.parse_args()

switcher = PyATEMMax.ATEMMax()
swsrc = PyATEMMax.ATEMVideoSources
sources = [swsrc.input1, swsrc.input2, swsrc.input3, swsrc.input4]

# Connect
switcher.connect(args.ip)
switcher.waitForConnection()

# switch based on input
switcher.setProgramInputVideoSource(0,sources[args.input-1])

switcher.disconnect()