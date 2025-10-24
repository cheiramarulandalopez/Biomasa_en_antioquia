// --- Funciones de cálculo ---

function calcularBiogas(residuosKg) {
  return residuosKg * 0.5; // 1 kg → 0.5 kWh
}

function calcularEficienciaEnergetica(energiaUtilizada, energiaProducida) {
  if (energiaUtilizada <= 0) throw new Error("La energía utilizada debe ser mayor que cero.");
  return ((energiaProducida / energiaUtilizada) * 100).toFixed(2);
}

// --- Botón 1: Calcular residuos orgánicos ---
document.getElementById("btnResiduos").addEventListener("click", () => {
  const residuos = parseFloat(document.getElementById("Residuosorganicos").value);
  const resultadoResiduos = document.getElementById("resultadoResiduos");

  if (isNaN(residuos) || residuos < 0) {
    resultadoResiduos.textContent = "⚠️ Ingresa una cantidad válida de residuos (en kg).";
    return;
  }

  const energia = calcularBiogas(residuos);
  let mensaje;
  if (energia >= 3) mensaje = "⚡ ¡Excelente! Esa energía podría alimentar varios electrodomésticos por un día.";
  else if (energia >= 1) mensaje = "🔋 Podrías cubrir la iluminación de tu casa por varias horas.";
  else mensaje = "🌱 Aunque es poca energía, ¡imagina el impacto si todos reciclaran!";

  resultadoResiduos.textContent = `A partir de ${residuos} kg de residuos, podrías generar ${energia.toFixed(2)} kWh. ${mensaje}`;
});

// --- Botón 2: Calcular eficiencia energética ---
document.getElementById("btnEficiencia").addEventListener("click", () => {
  const energiaUtilizada = parseFloat(document.getElementById("energiaUtilizada").value);
  const energiaProducida = parseFloat(document.getElementById("energiaProducida").value);
  const resultadoEficiencia = document.getElementById("resultadoEficiencia");

  if ([energiaUtilizada, energiaProducida].some(v => isNaN(v))) {
    resultadoEficiencia.textContent = "⚠️ Ingresa valores válidos en ambos campos.";
    return;
  }

  try {
    const eficiencia = calcularEficienciaEnergetica(energiaUtilizada, energiaProducida);
    resultadoEficiencia.textContent = `La eficiencia energética es del ${eficiencia}%`;
  } catch (error) {
    resultadoEficiencia.textContent = `❌ ${error.message}`;
  }
});
