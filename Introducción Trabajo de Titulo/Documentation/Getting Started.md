# Rendering Basic Concepts:
```js
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();

renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
        
```

Those 3 variables are essential to display something on screen. Naturally, there're important details related to each variable.

## Scene
Basically, is the canvas that's going to contain everything we're going to render. For example, if we want to render a cube, we have to create it and then "add" it to the scene. By default, every object added to the scene, is going to appear in the coordinates (0, 0, 0)

## Perspective Camera
- **First parameter:** FOV
- **Second parameter**: Screen Ratio
- **Third and fourth parameters**: Near and Far clipping plane. This values defines the min/max distance of rendering relative to the camera.


## Renderer
- Three.JS has different types of renderers, but usually is recommended use WebGL
- After creating `renderer`, we have to set the resolution of the app. This make possible to run an app in lower resolutions to improve performance


# Creating 3D Objects

```js
const geometry = new THREE.BoxGeometry(); 
const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } ); 
const cube = new THREE.Mesh( geometry, material ); 
scene.add( cube ); 

camera.position.z = 5;
```

1. ``BoxGeometry`` creates an object which contains all the points and faces of one cube
2. `material` as it's name suggest, define the material of which the 3D objects is made. For example, this specifies how the body is going to reflect light.
3. `Mesh` takes a 3D objects and applies a material to it. In this case, it made the cube green.
4. `scene.add(obj)` inserts an `obj` in the scene previously defined. Since no coordinates were specified, the cube is going to be rendered in the origin of the scene

# Render Loop
Due how computers works, we've to create a loop in charge of rendering the scene every time the screen is refreshed. To do so, we have to define a function in which the first line should call the method `requestAnimationFrame(func_loop);`. For example:

``` js
function animate() { 
	requestAnimationFrame( animate );
	cube.rotation.x += 0.01;
	cube.rotation.y += 0.01;
	renderer.render( scene, camera ); 
}; 

animate();
```

1. `requestAnimationFrame` has to receive the name of the function that invokes it to create the loop.
2. Then, we can do everything we want, whether modifying 3D objects, calculate something, manage logic of a game, etc. In this case, we're rotating a cube.
3. Finally, we have to render everything to see the modifications made in the previous points.


# Main Concepts
1. [[Render]]
2. [[Camera]]
3. [[Scene]]
4. [[Geometry]]
5. [[Material]]