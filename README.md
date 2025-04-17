# 🧠 Automatización de Consulta y Procesamiento de Datos - GTR Refrigerios

Este script fue creado para automatizar parte del proceso de monitoreo y gestión de tiempos de refrigerio del equipo de atención en la campaña **ATT**. Realiza la conexión a la base de datos, construye dataframes con información del personal, y lanza una interfaz con una cuenta regresiva visual para indicar cuándo iniciar una nueva consulta.

---

## 🛠️ Funcionalidades principales

- 🔐 **Desencripta credenciales** de conexión de forma segura.
- 🧾 **Consulta la nómina activa** en la campaña ATT desde una base de datos MySQL.
- 📊 Crea y organiza dataframes con pandas para:
  - Nómina de agentes
  - Conexiones activas
  - Tiempos en AUX o VDN
- ⏳ **Interfaz gráfica de cuenta regresiva** con `customtkinter` para indicar el inicio de una nueva consulta de tiempos.
- 🖥️ Ventana centrada y siempre en primer plano.

---


🧪 Estructura del script
iniciarconexion(...): Conecta a MySQL y devuelve un cursor.

iniciar_temporizador(segundos): Muestra una cuenta regresiva básica (segundos).

interfaceCuentaRegresiva(minutos): Muestra cuenta regresiva en formato mm:ss.

Se procesan los datos de la nómina para obtener un DataFrame limpio con nombres, apellidos y ID de Avaya.

🖼️ Ejemplo de salida
+----------+-------------------------------------------+
| ID_Avaya | Nombre                                    |
+----------+-------------------------------------------+
| 562833   | Caceres Pereira, Andres Federico          |
| 562765   | Rodriguez Alfonzo, Naiyely Hecnay         |
| ...      | ...                                       |
+----------+-------------------------------------------+

En base a esta salida se ejecuta una alerta automatica que se envia a un grupo de Whatsapp con el siguiente formato:
En caso de ser una alerta de exceso de auxiliar:

Sistema de alertas automáticas: 
 
[ Orozco, Mariano ] "HOLD" con: 8.6 minutos.


🧠 Funciones adicionales importantes
consulta_dimensionamiento_ppp(fecha, intervalo, skill)
Consulta los datos de pronóstico para una campaña y skill específicos desde la base de datos, como:

Volumen esperado

TMO planificado

Ausentismo e improductividad estimados

Requerimiento de personal (DIM, RACS, PSTAFF, Erlang)

🔍 Usa esta información para comparar con métricas reales y tomar decisiones.

Evalúa si se deben:

Suspender auxiliares,

Permitir auxiliares no programados,

Emitir alertas por exceso en el TMO.

Variables evaluadas:

Nivel de servicio (nds)

Tiempo de llamada más antigua (oldest)

Asesores en auxiliar (reps_auxiliares)

Staff total (staff)

Disponibles (reps_avail)

TMO real vs TMO planificado

Ocupación

Llamadas en espera

Ejemplo de alerta generada:
Campaña X
Alerta: Suspender auxiliares
> Nivel de servicio: 92%
> Ocupación: 100%
> Llamadas en espera: 5
> Llamada más antigua: 00:45
> Agentes en auxiliar: 6 - 20 (30.0% del staff en AUX)


Whatsapp(grupoWSP)
Envía alertas automáticamente a un grupo de WhatsApp abriendo la app, pegando el mensaje desde el portapapeles y cerrando. 

segundos_a_hms(segundos)
Convierte segundos a formato mm:ss para mostrar tiempos de espera de llamadas de forma legible.

📊 Ejemplo de flujo de uso
El script arranca, obtiene la fecha actual y ajusta el intervalo horario al formato cerrado (08:00, 08:30, etc.).

Se consulta el pronóstico del skill correspondiente con consulta_dimensionamiento_ppp().

Se scrapean los datos reales (TMO, ocupación, llamadas en espera).

Se evalúan decisiones con evaluear_decisiones() y se generan alertas.

Las alertas se copian al portapapeles o se envían por WhatsApp automáticamente.
