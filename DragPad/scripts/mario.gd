extends Node2D

const SPEED = 5
const AnSPEED = 0.5

var speed_x = 0
var speed_y = 0

var omega = 0

# Called when the node enters the scene tree for the first time.
func _ready():
	position.x = 800
	position.y = 400


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if Input.is_key_pressed(KEY_W):
		speed_y = -SPEED
	elif Input.is_key_pressed(KEY_S):
		speed_y = SPEED
	elif Input.is_key_pressed(KEY_A):
		speed_x = -SPEED
	elif Input.is_key_pressed(KEY_D):
		speed_x = SPEED
	elif Input.is_key_pressed(KEY_R):
		position.x = 800
		position.y = 400
	elif Input.is_key_pressed(KEY_LEFT):
		omega = -AnSPEED
	elif Input.is_key_pressed(KEY_RIGHT):
		omega = AnSPEED
	else:
		speed_x = 0
		speed_y = 0
		omega = 0
	position.x += speed_x
	position.y += speed_y
	rotate(omega)
	
func _on_bu_button_down():
	speed_y = -SPEED
	
func _on_bu_button_up():
	speed_y = 0

func _on_bd_button_down():
	speed_y = SPEED

func _on_bd_button_up():
	speed_y = 0

func _on_br_button_down():
	speed_x = SPEED

func _on_br_button_up():
	speed_x = 0

func _on_bl_button_down():
	speed_x = -SPEED

func _on_bl_button_up():
	speed_x = 0

func _on_reset_pressed():
	position.x = 800
	position.y = 400

func _on_button_r_right_button_up():
	omega = 0

func _on_button_r_left_button_up():
	omega = 0

func _on_button_r_left_button_down():
	omega = -AnSPEED

func _on_button_r_right_button_down():
	omega = AnSPEED
