extends Node2D

@export var amplitude = 300

# Enviar señales
signal touch()
signal moving_player_pressed()

var accum_time=0
var next_x_pos=0
var offset = Vector2(300,300)
var speed = 1.0
# Called when the node enters the scene tree for the first time.
func _ready():
	position.y = offset.y
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	accum_time += delta
	next_x_pos = offset.x + amplitude* sin(speed * accum_time)
	if next_x_pos > 400:
		print('Senial emitida')
		touch.emit()
	position.x = next_x_pos


func _on_button_button_down():
	amplitude += 50
