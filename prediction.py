from nicegui import ui

grid = [[0] * 28 for _ in range(28)]

def create_grid():
    with ui.grid(columns=28).classes('gap-0'):
        for i in range(28):
            for j in range(28):
                btn = ui.button('').style('width: 20px; height: 20px; padding: 0px; background: white')
                btn.i = i
                btn.j = j
                def click(e):
                    e.sender.style('background: black')
                    grid[e.sender.i][e.sender.j] = 1
                btn.on_click(click)

ui.button('Clear')
create_grid()

ui.run()
