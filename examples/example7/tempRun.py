import shutil
MainWindow.clearData()
examplePath = "E:/FastCAE/FastCAE_master/output/examples/example7"
dirPath = examplePath + "/../../"
desC = dirPath + "ConfigFiles"
dess = dirPath + "solver"
if os.path.exists(desC): shutil.rmtree(desC)
if os.path.exists(dess): shutil.rmtree(dess)
shutil.copytree(examplePath + "/ConfigFiles/", dirPath + "ConfigFiles/")
shutil.copytree(examplePath + "/solver/", dirPath + "Solver/")
MainWindow.updateInterface()
MainWindow.openProjectFile("E:/FastCAE/FastCAE_master/output/examples/example7/M99.diso")
MainWindow.solveProject(0,0)
