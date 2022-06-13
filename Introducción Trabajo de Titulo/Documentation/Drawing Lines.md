# How create a Line

## [[Material]]
To create a line, we have to use a material specifically designed to create lines, for example, `LineBasicMaterial`  or `LineDashedMaterial`.

```js
const material = new THREE.LineBasicMaterial( { color: 0x0000ff } );
```

## [[Geometry]]
The geometry of one line is composed by multiple points/vertices which we could manually define. For example:
``` js
const points = []; 
points.push( new THREE.Vector3( - 10, 0, 0 ) ); 
points.push( new THREE.Vector3( 0, 10, 0 ) );
points.push( new THREE.Vector3( 10, 0, 0 ) );
const geometry = new THREE.BufferGeometry().setFromPoints( points );
```
Here, we can notice how we defined 3 vertices and then put them in an array. Then, we pass said array to `BufferGeometry`
>  [BufferGeometry](https://threejs.org/docs/#api/en/core/BufferGeometry) is a representation of mesh, line, or point geometry. Includes vertex positions, face indices, normals, colors, UVs, and custom attributes within buffers, reducing the cost of passing all this data to the GPU. 
>  
>  Also, it's easily customizable allowing the user modifying the object defined using BufferGeometry whenever they want.