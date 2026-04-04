// Animated azulejo banner — "Ribeira waves, sky" variant.
// Auto-initializes every <canvas class="azulejo-banner"> on the page.
// Fixed palette: does NOT react to dark/light mode.
(function () {
  const VS = `attribute vec2 a_pos; void main(){ gl_Position=vec4(a_pos,0.0,1.0); }`;

  const FS = `
    precision highp float;
    uniform vec2 u_res;
    uniform float u_time;

    float fill(float d){
      float aa = fwidth(d)*1.2;
      return 1.0 - smoothstep(-aa, aa, d);
    }
    float line(float d, float w){
      float aa = fwidth(d)*1.2;
      return 1.0 - smoothstep(w-aa, w+aa, abs(d));
    }

    void main(){
      vec2 uv = gl_FragCoord.xy/u_res.y;
      uv.x -= 0.5*u_res.x/u_res.y;
      float t = u_time*0.4;

      vec3 sky  = vec3(0.071, 0.161, 0.349); // #122959
      vec3 foam = vec3(0.957, 0.937, 0.902); // #F4EFE6
      vec3 col  = sky;

      for (int i=0; i<5; i++){
        float fi = float(i);
        float y = -0.35 + fi*0.18;
        float wave = y + 0.06*sin(uv.x*6.0 + t + fi*1.3)
                       + 0.03*sin(uv.x*13.0 - t*1.2 + fi);
        float d = uv.y - wave;
        vec3 c = mix(vec3(0.45, 0.62, 0.82), vec3(0.07, 0.16, 0.35), fi/4.0);
        col = mix(col, c, fill(-d));
        col = mix(col, foam, line(d, 0.006));
      }

      for (int i=0; i<5; i++){
        float fi = float(i);
        float y = -0.35 + fi*0.18;
        float wave = y + 0.06*sin(uv.x*6.0 + t + fi*1.3)
                       + 0.03*sin(uv.x*13.0 - t*1.2 + fi);
        float dx = fract(uv.x*3.0 + fi*0.3 + t*0.1) - 0.5;
        float d = length(vec2(dx*0.3, uv.y - wave - 0.03)) - 0.012;
        col = mix(col, foam, fill(d));
      }

      gl_FragColor = vec4(col, 1.0);
    }
  `;

  function init(canvas) {
    const gl = canvas.getContext("webgl", { antialias: true });
    if (!gl) return;
    const ext = gl.getExtension("OES_standard_derivatives");
    const header = ext ? "#extension GL_OES_standard_derivatives : enable\n" : "";

    function compile(type, src) {
      const s = gl.createShader(type);
      gl.shaderSource(s, src);
      gl.compileShader(s);
      if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
        console.error("azulejo-banner:", gl.getShaderInfoLog(s));
      }
      return s;
    }

    const prog = gl.createProgram();
    gl.attachShader(prog, compile(gl.VERTEX_SHADER, VS));
    gl.attachShader(prog, compile(gl.FRAGMENT_SHADER, header + FS));
    gl.linkProgram(prog);
    gl.useProgram(prog);

    const buf = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(
      gl.ARRAY_BUFFER,
      new Float32Array([-1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1]),
      gl.STATIC_DRAW,
    );
    const loc = gl.getAttribLocation(prog, "a_pos");
    gl.enableVertexAttribArray(loc);
    gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);

    const uRes = gl.getUniformLocation(prog, "u_res");
    const uTime = gl.getUniformLocation(prog, "u_time");

    function resize() {
      const r = canvas.getBoundingClientRect();
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.max(1, Math.floor(r.width * dpr));
      canvas.height = Math.max(1, Math.floor(r.height * dpr));
      gl.viewport(0, 0, canvas.width, canvas.height);
    }
    resize();
    window.addEventListener("resize", resize);

    const start = performance.now();
    let running = true;

    // Pause when offscreen to save cycles
    const io = new IntersectionObserver(
      (entries) => entries.forEach((e) => (running = e.isIntersecting)),
      { threshold: 0 },
    );
    io.observe(canvas);

    function frame() {
      if (running) {
        gl.uniform2f(uRes, canvas.width, canvas.height);
        gl.uniform1f(uTime, (performance.now() - start) / 1000);
        gl.drawArrays(gl.TRIANGLES, 0, 6);
      }
      requestAnimationFrame(frame);
    }
    frame();
  }

  function boot() {
    document.querySelectorAll("canvas.azulejo-banner").forEach(init);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
