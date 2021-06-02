b = 0
game.splash("start")

def on_forever():
    global b
    MCP23017.write_pin(0, b)
    a = MCP23017.mytest(0)
    b = b + 1
    game.splash(a, "b=" + ("" + str(b)))
forever(on_forever)
