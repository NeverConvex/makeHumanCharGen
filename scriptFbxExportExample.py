import os
import numpy

# Can't just pass an exporter a path, must give it a validation function
def filename(targetExt, different = False):
   global name, dir
   if targetExt.lower() != 'fbx':
      log.warning("expected extension '.%s' but got '%s'", targetExt,  'fbx')
   return os.path.join(dir, name + '.' + targetExt)

params = str(MHScript.getModelingParameters)
print("params =")
print(params)
MHScript.printDetailStack()

def getPath(x):
    global weight, age
    return 'C:/Users/NeverConvex/Desktop/Game Creation/MakeHuman_ScriptExperiments/goblinMadeHumans/goblin_weight'+str(weight)+'_age'+str(age)+'.fbx'

for weight in numpy.arange(0,1,0.05):
    #for height in numpy.arange(0,1,0.05):
    for age in numpy.arange(0,1,0.05):
        # Export file path
        #path = '/c/Users/NeverConvex/Desktop/Game Creation/MakeHuman_ScriptExperiments/test.fbx'
        path = '/c/Users/NeverConvex/Desktop/Game Creation/MakeHuman_ScriptExperiments/goblinMadeHumans/goblin_weight'+str(weight)+'_age'+str(age)+'.fbx'
        dir, name = os.path.split(path)
        name, ext = os.path.splitext(name)

        # Getting current export path so we can reset it later
        curExportdir = G.app.getSetting('exportdir')

        G.app.setSetting('exportdir', dir)

        # Getting human to export
        human = G.app.selectedHuman

        # Getting exporter and exporting fbx
        MHScript.setWeight(weight)
        MHScript.setAge(age)
        exporter = G.app.getCategory('Files').getTaskByName('Export').getExporter('Filmbox (fbx)')
        #exporter.export(human, filename)
        #exporter.export(human, lambda x: global weight; global age; '/c/Users/NeverConvex/Desktop/Game Creation/MakeHuman_ScriptExperiments/goblinMadeHumans/goblin_weight'+weight+'_age'+age+'.fbx')
        exporter.export(human, getPath)
    
        # Resetting exportdir
        G.app.setSetting('exportdir', curExportdir)
