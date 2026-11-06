export default function HomePage() {
  return (
    <main style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>AIDD Platform — Next.js 16 + FastAPI + Keycloak</h1>
      <p>Орталық білім беру және жергілікті LLM (Ollama) платформасы.</p>
      <ul>
        <li>FastAPI Backend: <a href="http://localhost:8000/docs">/docs</a></li>
        <li>Keycloak Auth: <a href="http://localhost:8080">Keycloak Console</a></li>
        <li>Ollama LLM: http://localhost:11434</li>
      </ul>
    </main>
  );
}
