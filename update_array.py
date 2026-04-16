import re
import json

with open('c:/Users/Usuario/Documents/Proyectos/robotica/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the robots array string
match = re.search(r'const robots = (\[\s*\{.*?\}\s*\]);', html, re.DOTALL)
if not match:
    print("Could not find robots array")
    exit(1)

robots_str = match.group(1)

# A manual parse/replace approach for each ID
replacements = {
    10: 'image: "Victor_Scheinman_at_MIT_Museum.agr.jpg"',
    11: 'image: "WABOT-1-1973.jpg"',
    12: 'youtubeShortId: "1iMXrb5SW8s"',
    13: 'image: "Genghis_Robot.jpg"',
    14: 'image: "dante2-horizontal.jpg"',
    15: 'image: "RoboTuna,_1994,_view_2_-_MIT_Museum_-_DSC03730.jpg"',
    16: 'youtubeShortId: "4xSXWMa-jQ8"',
    17: 'youtubeVideoId: "I-tCRtb6qag"',
    # 18 ASIMO skipped
    19: 'youtubeShortId: "Zb7742vk1PM"',
    20: 'youtubeShortId: "HL6sJt2Pmo8"',
    21: 'youtubeShortId: "JtzeOPHJ5yQ"',
    22: 'image: "daVinciR-platforms-upgrading-through-the-years-from-1998-with-the-first-standard-model.webp"',
    23: 'youtubeShortId: "Ud2oH9cwpV8"',
    24: 'youtubeShortId: "-smO8NWLCss"',
    25: 'youtubeShortId: "ft7-wuH4ZFs"',
    26: 'youtubeShortId: "hxSZQ6Wfh-E"',
    27: 'youtubeShortId: "83SQmj5bF9A"',
    28: 'youtubeShortId: "gOYAfEOeg1Y"',
    29: 'youtubeShortId: "h4SQUglSsH4"',
    30: 'youtubeShortId: "yMQP6mB8_ac"',
    31: 'youtubeShortId: "e2gsHlC2HvM"'
}

# The objects are like:
#        {
#            id: 10,
#            nombre: "Stanford Arm",
#            ...
#            youtubeTimestamp: 240
#        },

for rid, props in replacements.items():
    # Find the object block for rid
    # It might already have a youtubeTimestamp at the end. We append the new prop.
    # regex to find the block:
    # id: 10,[\s\S]*?(youtubeTimestamp: \d+|youtubeShortId: "[^"]+")(\s*\n\s*})
    pattern = r'(id: ' + str(rid) + r',[\s\S]*?(?:youtubeTimestamp: \d+|youtubeShortId: "[^"]+"))(\s*\n\s*\})'
    
    def repl(m):
        # Instead of replacing, just append the new property if it doesn\'t exist
        text = m.group(1)
        if 'youtubeShortId' in text or 'image:' in text or 'youtubeVideoId' in text:
            # We don't touch it if we already replaced it or it was there (like the first 9)
            pass
        # Remove youtubeTimestamp if it's being replaced by something else?
        # Actually it's fine to keep youtubeTimestamp, or we can just append it:
        return text + ',\n            ' + props + m.group(2)

    robots_str = re.sub(pattern, repl, robots_str)

# Now append the new robots at the end of the array before the last ]
new_robots = """,
        {
            id: 32,
            nombre: "Unitree H1 / G1",
            año: 2023,
            yearDisplay: "2023-2024",
            creador: "Unitree Robotics",
            era: "Modelos Fundacionales",
            arquitectura: "VLA / Humanoid",
            descripcion: "Robots humanoides de origen chino diseñados para alta movilidad y accesibilidad comercial. El modelo H1 destacó por su récord de velocidad (3.3 m/s), mientras que el G1 ('Humanoid Agent') incorpora manos diestras de 3 dedos, visión 3D y fue presentado a un precio sumamente competitivo, marcando la era de los humanoides de consumo masivo.",
            etiquetas: ["Humanoide", "China", "Unitree", "Velocidad", "Mass Market"],
            youtubeVideoId: "I_CokTfF-bA"
        },
        {
            id: 33,
            nombre: "Fourier GR-1",
            año: 2023,
            yearDisplay: "2023",
            creador: "Fourier Intelligence",
            era: "Modelos Fundacionales",
            arquitectura: "General Purpose / Salud",
            descripcion: "Humanoide biomimético de propósito general desarrollado en China, enfocado inicialmente en rehabilitación y cuidado médico terapéutico. Con gran capacidad de carga y potentes actuadores articulares en la cadera, representa la entrada de los robots de asistencia geriátrica y médica al mercado global de las IA corporizadas.",
            etiquetas: ["Humanoide", "Salud", "China", "Asistencia", "Carga"],
            youtubeVideoId: "D8e1K9eB7_w"
        },
        {
            id: 34,
            nombre: "Olaf Robot",
            año: 2026,
            yearDisplay: "2026",
            creador: "Disney Imagineering & NVIDIA",
            era: "Modelos Fundacionales",
            arquitectura: "RL / Sim-to-Real (Kamino)",
            descripcion: "Robot interactivo de tamaño libre diseñado para los parques de Disney, basado en el personaje Olaf de Frozen. Utiliza un modelo de Inteligencia Artificial entrenado con Deep Reinforcement Learning en la plataforma Kamino de Disney y simulado en la nube usando motores de físicas como Newton (ahora abierto). Logra su característico deslizar de nieve con estabilidad autónoma sin programación mecánica explícita de trayectorias.",
            etiquetas: ["Entretenimiento", "Reinforcement Learning", "Sim-to-Real", "Disney"]
            // No image or video string provided, will fallback cleanly when there's none
        }
    """

robots_str = robots_str[:-1] + new_robots + "]"

html = html[:match.start()] + 'const robots = ' + robots_str + ';' + html[match.end():]

with open('c:/Users/Usuario/Documents/Proyectos/robotica/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated robots array")
