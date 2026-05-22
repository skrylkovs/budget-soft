// Блок 9a. 3D-сцена для featured-кейса (Three.js).
// Вращающийся «процессорный» каркас как абстрактный визуал продукта.
// Деградирует на статичный градиент при отсутствии WebGL или prefers-reduced-motion.
import * as THREE from 'three';

const mount = document.getElementById('case3d');
if (mount) {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  } catch (e) {
    renderer = null;
  }

  if (renderer) {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 100);
    camera.position.set(0, 0, 6);

    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setClearColor(0x000000, 0);
    mount.appendChild(renderer.domElement);

    // Икосаэдр-каркас + ядро
    const group = new THREE.Group();
    const wire = new THREE.Mesh(
      new THREE.IcosahedronGeometry(1.7, 1),
      new THREE.MeshBasicMaterial({ color: 0x8366ff, wireframe: true, transparent: true, opacity: 0.65 })
    );
    const core = new THREE.Mesh(
      new THREE.IcosahedronGeometry(1.05, 0),
      new THREE.MeshStandardMaterial({ color: 0xb14bff, emissive: 0x4a1f8a, metalness: 0.4, roughness: 0.3, flatShading: true })
    );
    group.add(wire, core);
    scene.add(group);

    scene.add(new THREE.AmbientLight(0xffffff, 0.5));
    const key = new THREE.PointLight(0xff4ec0, 60, 50);
    key.position.set(5, 5, 5);
    const fill = new THREE.PointLight(0x4ea8ff, 40, 50);
    fill.position.set(-5, -3, 4);
    scene.add(key, fill);

    const resize = () => {
      const w = mount.clientWidth || 1;
      const h = mount.clientHeight || 1;
      renderer.setSize(w, h, false);
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
    };
    resize();
    window.addEventListener('resize', resize);

    // Mouse-follow parallax
    const target = { x: 0, y: 0 };
    mount.closest('.case-featured')?.addEventListener('mousemove', (e) => {
      const r = mount.getBoundingClientRect();
      target.x = ((e.clientX - r.left) / r.width - 0.5) * 0.6;
      target.y = ((e.clientY - r.top) / r.height - 0.5) * 0.6;
    });

    const animate = () => {
      group.rotation.y += reduce ? 0 : 0.004;
      group.rotation.x += (target.y - group.rotation.x) * 0.05;
      group.rotation.z += (target.x - group.rotation.z) * 0.05;
      renderer.render(scene, camera);
      requestAnimationFrame(animate);
    };
    if (reduce) renderer.render(scene, camera);
    else animate();
  } else {
    mount.style.background = 'radial-gradient(circle at 60% 40%, rgba(177,75,255,0.4), transparent 60%)';
  }
}
