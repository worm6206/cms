print('start ...')
from browser import doc, window
from javascript import JSObject,JSConstructor
import math

gridX = true
gridY = false
gridZ = false
axes = true
ground = true
effectController = {}
canvasWidth = window.innerWidth
canvasHeight = window.innerHeight
print(canvasWidth, canvasHeight)

# good
def createRobotExtender(part, length, material):
    cylindergeometryC = JSConstructor(THREE.CylinderGeometry)
    cylindergeometry = cylindergeometryC(22, 22, 6, 32)
    meshC = JSConstructor(THREE.Mesh)
    cylinder = meshC(cylindergeometry, material)
    part.add(cylinder)
    for i in range(4):
        cubegeometryC = JSConstructor(THREE.CubeGeometry)
        cubegeometry = cubegeometryC(4, length, 4)
        meshC = JSConstructor(THREE.Mesh)
        box = meshC(cubegeometry, material)
        if i <2:
            box.position.x = -8
        else:
            box.position.x = 8
        box.position.y = length/2
        if i%2:
            box.position.z = -8
        else:
            box.position.z = 8
        part.add( box )

    cylindergeometry = cylindergeometryC(15, 15, 40, 32)
    meshC = JSConstructor(THREE.Mesh)
    cylinder = meshC(cylindergeometry, material)
    cylinder.rotation.x = 90 * math.pi/180
    cylinder.position.y = length
    part.add(cylinder)

# good
def createRobotCrane(part, length, material):
    cubegeometryC = JSConstructor(THREE.CubeGeometry)
    cubegeometry = cubegeometryC(18, length, 18)
    meshC = JSConstructor(THREE.Mesh)
    box = meshC(cubegeometry, material)
    box.position.y = length/2
    part.add(box)
    spheregeometryC = JSConstructor(THREE.SphereGeometry)
    spheregeometry = spheregeometryC(20, 32, 16)
    meshC = JSConstructor(THREE.Mesh)
    sphere = meshC(spheregeometry, material)
    # place sphere at end of arm
    sphere.position.y = length
    part.add(sphere)

def setupGui():
    global effectController
    effectController = {
    	"newGridX": gridX,
		"newGridY": gridY,
		"newGridZ": gridZ,
		"newGround": ground,
		"newAxes": axes,
		
		"uy": 70.0,
		"uz": -15.0,

		"fy": 10.0,
		"fz": 60.0
	}
    guiC = JSConstructor(dat.GUI)
    gui = guiC()
    h = gui.addFolder("Grid display")
    h.add(effectController, "newGridX").name("Show XZ grid")
    h.add(effectController, "newGridY" ).name("Show YZ grid")
    h.add(effectController, "newGridZ" ).name("Show XY grid")
    h.add(effectController, "newGround" ).name("Show ground")
    h.add(effectController, "newAxes" ).name("Show axes")
    '''
    h = gui.addFolder("Arm angles")
    h.add(effectController, "uy", list(range(-180, 180, 1))).name("Upper arm y")
    h.add(effectController, "uz", -45.0, 45.0, 0.025).name("Upper arm z")
    h.add(effectController, "fy", -180.0, 180.0, 0.025).name("Forearm y")
    h.add(effectController, "fz", -120.0, 120.0, 0.025).name("Forearm z")
    '''

cameraC = JSConstructor( THREE.PerspectiveCamera )
camera = cameraC( 75, 1, 1, 10000 )
camera.position.z = 1000;

sceneC = JSConstructor( THREE.Scene );
scene = sceneC();

geometryC = JSConstructor(THREE.CubeGeometry)
geometry = geometryC(200, 200, 200)
materialC = JSConstructor( THREE.MeshBasicMaterial )

material = materialC( { "color": "#ff0000", "wireframe": True } )

meshC = JSConstructor(THREE.Mesh)
mesh = meshC(geometry, material)
scene.add(mesh);

# materialC
materialC = JSConstructor(THREE.MeshPhongMaterial )
robotBaseMaterial  = materialC({"color": 0x6E23BB, "specular": 0x6E23BB, "shininess": 20})
robotForearmMaterial = materialC({"color": 0xF4C154, "specular": 0xF4C154, "shininess": 100})
robotUpperArmMaterial = materialC({"color": 0x95E4FB, "specular": 0x95E4FB, "shininess": 100})

torusgeometryC = JSConstructor(THREE.TorusGeometry)
torusgeometry = torusgeometryC(22, 15, 32, 32)

# torus
meshC = JSConstructor(THREE.Mesh)
torus = meshC(torusgeometry, robotBaseMaterial)
scene.add(torus)

# forearm
object3DC = JSConstructor(THREE.Object3D)
forearm = object3DC()
faLength = 80
createRobotExtender(forearm, faLength, robotForearmMaterial)

arm = object3DC()
uaLength = 120
createRobotCrane(arm, uaLength, robotUpperArmMaterial)

# Move the forearm itself to the end of the upper arm.
forearm.position.y = uaLength
arm.add(forearm)
scene.add(arm)

rendererC = JSConstructor(THREE.CanvasRenderer)
renderer = rendererC({ "antialias": true } )
renderer.gammaInput = true
renderer.gammaOutput = true
renderer.setSize(canvasWidth, canvasHeight)
renderer.setClearColorHex( 0xAAAAAA, 1.0 )


doc['container'] <= renderer.domElement
renderer.render( scene, camera )

def animate(i):
    # note: three.js includes requestAnimationFrame shim
    requestAnimationFrame( animate );

    mesh.rotation.x += 0.01;
    mesh.rotation.y += 0.02;

    renderer.render( scene, camera );   

setupGui()
animate(0)
