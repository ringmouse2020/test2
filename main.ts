let b = 0
game.splash("start")
forever(function () {
    MCP23017.WritePin(0, b)
let a = MCP23017.Mytest(0)
b = b + 1
    game.splash(a, "b=" + ("" + b))
})
