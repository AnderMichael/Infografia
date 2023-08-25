extends Node2D

const MAX_SPEED = 80
var health = 10
# Tipar variables - posicion modificable
var target_position : Vector2 = Vector2(0,0)
# Exportar una variable 
@export var init_speed = 10

# Called when the node enters the scene tree for the first time.
func _ready():
	print("Iniciamos el nodooooo")
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	position = target_position
	pass

# Recibe un evento
func _input(event):
	if event is InputEventMouseMotion:
		print(event.position)
		target_position = event.position
	if (event is InputEventKey 
	and event.is_pressed() and event.as_text_key_label() == 'R'):
		rotate(0.5)
	
