import arcade

width = 600
height = 600
title = 'Welcome'

radius = 100

arcade.open_window(width, height, title)
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

arcade.draw_circle_filled(width / 2, height / 2, radius, arcade.color.BLUE)


arcade.finish_render()
arcade.run()
