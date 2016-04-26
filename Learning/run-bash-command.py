# Run the setup file for this workspace

# http://stackoverflow.com/a/4256143/893511
import subprocess, os
SOURCEDIR = os.path.dirname(os.path.abspath(__file__)) # URL: http://stackoverflow.com/a/7783326
commandStr = "source"
subDirStr = "/devel/setup.bash"
pathStr = os.path.join(SOURCEDIR + subDirStr)
bashStr = commandStr + " " + pathStr
try:
    process = subprocess.Popen(bashStr.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print "Command '",bashStr,"' was succesful"
except Exception as err:
    print "Command '",bashStr,"' was NOT succesful"
    print "Encountered" , type(err).__name__ , "with args:", err.args,"with full text:",str(err)
        
