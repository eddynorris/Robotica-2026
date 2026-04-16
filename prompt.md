Rol: Eres un Ingeniero Frontend Senior experto en Vanilla JavaScript, HTML5 y Tailwind CSS.

Objetivo: Desarrollar una aplicación web interactiva en un único archivo index.html (usando Tailwind CSS vía CDN) que funcione como un "Museo Interactivo de la Robótica". La aplicación debe documentar la evolución de los robots basándose en el video de YouTube "Evolution Of Robots" (ID: hft_i3TpRok).

Arquitectura de Datos (JSON Local):
Dentro de una etiqueta <script>, crea un array de objetos con absolutamente todos los robots mencionados en el video (desde Talos, Unimate y Shakey, hasta Asimo, Atlas de Boston Dynamics, Optimus de Tesla, Figure 01, y el proyecto GR00T de NVIDIA).
Cada objeto debe tener la siguiente estructura:

id, nombre, año, creador, era (categoría).

arquitectura (ej. Reactiva, Deliberativa, VLA).

descripcion (un párrafo técnico y conciso sobre su hito).

etiquetas (array de strings como "Lazo Abierto", "Hidráulico", "SLAM", "Transformers").

youtubeTimestamp (el segundo exacto en el que aparece en el video, ej. 125 para el minuto 2:05).

UI/UX y Flujo de Interacción:

Estilo General: "Dark Mode" tecnológico (fondos bg-slate-900, texto claro, acentos en cian y azul). Tipografía sans-serif limpia.

Navegación por Pestañas (Eras): En la parte superior, botones para filtrar la línea de tiempo por eras (ej. "Mitos", "Industriales", "Era de la Percepción", "Modelos Fundacionales").

Línea de Tiempo (Timeline): Debajo de las pestañas, renderiza una línea de tiempo horizontal o vertical. Cada robot es un "nodo" o punto brillante en la línea con su año visible. Al pasar el cursor, debe mostrar un tooltip con el nombre del robot.

Panel de Detalles (Modal/Drawer): Al hacer clic en un nodo de la línea de tiempo, se debe abrir un modal central o un panel lateral superpuesto.

Contenido del Modal:

Reproductor de Video: Un iframe de YouTube incrustado dinámicamente que apunte al video original, iniciando en el timestamp específico del robot (src="https://www.youtube.com/embed/hft_i3TpRok?start=${youtubeTimestamp}&autoplay=1").

Ficha Técnica: Título (Nombre), Año, Creador y Arquitectura renderizados de forma elegante.

Descripción y Badges: El texto explicativo y los badges visuales (usando clases de Tailwind como bg-blue-900 text-blue-300 rounded-full px-2 py-1) con las etiquetas técnicas.

Requerimientos Técnicos Obligatorios:

TODO el código (HTML, CSS personalizado mínimo, y lógica JS) debe estar contenido en un solo bloque listo para copiarse y guardarse como index.html.

Utiliza FontAwesome vía CDN o SVGs en línea para los iconos (ej. botón de cerrar modal).

Asegúrate de que la transición entre estados (abrir/cerrar modal, cambiar pestañas) sea fluida mediante clases de utilidad de transición de Tailwind (transition-all duration-300).