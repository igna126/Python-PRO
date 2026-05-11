import discord
from discord.ext import commands

# =========================
# BASE DE DATOS DE OBJETOS
# =========================

OBJETOS = {
    "botella de plástico": {
        "reciclable": True,
        "tiempo_descomposicion": "450 años"
    },

    "bolsa de plástico": {
        "reciclable": True,
        "tiempo_descomposicion": "10-20 años"
    },

    "caja de cartón": {
        "reciclable": True,
        "tiempo_descomposicion": "2 meses"
    },

    "cepillo de dientes": {
        "reciclable": False,
        "tiempo_descomposicion": "500 años",
        "manualidad": "Puedes usarlo para limpiar esquinas o teclados."
    },

    "pilas": {
        "reciclable": False,
        "tiempo_descomposicion": "100 años",
        "manualidad": "Llévalas a un centro especializado."
    }
}

# =========================
# CONFIGURACIÓN DEL BOT
# =========================

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# =========================
# EVENTO DE INICIO
# =========================

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

# =========================
# COMANDO: !eco
# =========================

@bot.command()
async def eco(ctx, *, objeto):

    objeto = objeto.lower()

    if objeto in OBJETOS:

        datos = OBJETOS[objeto]

        mensaje = f"🌎 **Información sobre:** {objeto}\n\n"

        if datos["reciclable"]:
            mensaje += "♻️ Reciclable: Sí\n"
        else:
            mensaje += "❌ Reciclable: No\n"

        mensaje += f"⏳ Tiempo de descomposición: {datos['tiempo_descomposicion']}\n"

        if "manualidad" in datos:
            mensaje += f"💡 Idea útil: {datos['manualidad']}"

        await ctx.send(mensaje)

    else:
        await ctx.send("⚠️ Ese objeto no está en la base de datos.")

# =========================
# COMANDO: !objetos
# =========================

@bot.command()
async def objetos(ctx):

    lista = "\n".join(OBJETOS.keys())

    await ctx.send(f"📦 Objetos disponibles:\n\n{lista}")

# =========================
# TOKEN DEL BOT
# =========================

bot.run
