import PySimpleGUI as sg

sg.theme("Black")

def gen_inertia(ixx,iyy,izz):
    inertiastr = "<inertial>\n<origin xyz=\"0 0 0\"/>\n<mass value=\"{0}\"/>\n<inertia ixx=\"{1:.10f}\" ixy=\"0\" ixz=\"0\" iyy=\"{2:.10f}\"  iyz=\"0\" izz=\"{3:.10f}\"/>\n</inertial>".format(weight,ixx,iyy,izz)
    sg.popup_scrolled(inertiastr)

def get_params(values):
    global weight
    global bar_length,bar_radius
    global sphere_radius
    global long_sphere_a,long_sphere_b,long_sphere_c
    global cylinder_radius ,cylinder_height
    global cylinder_hole_radius1,cylinder_hole_radius2
    global box_width,box_height,box_depth
    global circular_cone_radius,circular_cone_height

    weight = float(values[0])
    bar_length,bar_radius = float(values[1]),float(values[2])
    sphere_radius = float(values[3])
    long_sphere_a,long_sphere_b,long_sphere_c = float(values[4]),float(values[5]),float(values[6])
    cylinder_radius ,cylinder_height = float(values[7]),float(values[10])
    cylinder_hole_radius1,cylinder_hole_radius2 = float(values[8]),float(values[9])
    box_width,box_height,box_depth = float(values[11]),float(values[12]),float(values[13])
    circular_cone_radius,circular_cone_height = float(values[14]),float(values[15])

def bar_side():
    print(bar_length,bar_radius)
    ixx = (1./3.)*weight*bar_length ** 2
    iyy = 0
    izz = (1./3.)*weight*bar_length ** 2
    gen_inertia(ixx,iyy,izz)

def circular_cone():
    print(circular_cone_height,circular_cone_radius)
    ixx = (3./5.)*weight*circular_cone_height ** 2 + (3./20.)*weight*circular_cone_radius ** 2
    iyy = (3./5.)*weight*circular_cone_height ** 2 + (3./20.)*weight*circular_cone_radius ** 2
    izz = (3./10.)*weight*circular_cone_radius ** 2
    gen_inertia(ixx,iyy,izz)

def empty_sphere():
    print(sphere_radius)
    ixx = (2./3.)*weight*sphere_radius ** 2
    iyy = (2./3.)*weight*sphere_radius ** 2
    izz = (2./3.)*weight*sphere_radius ** 2
    gen_inertia(ixx,iyy,izz)

def bar_center():
    print(bar_length,bar_radius)
    ixx = (1./12.)*weight*bar_length ** 2
    iyy = 0
    izz = (1./12.)*weight*bar_length ** 2
    gen_inertia(ixx,iyy,izz)

def sphere():
    print(sphere_radius)
    ixx = (2./5.)*weight*sphere_radius ** 2
    iyy = (2./5.)*weight*sphere_radius ** 2
    izz = (2./5.)*weight*sphere_radius ** 2
    gen_inertia(ixx,iyy,izz)

def hole_cylinder():
    print(cylinder_height,cylinder_hole_radius1,cylinder_hole_radius2)
    ixx = (1./12.)*weight*(3*(cylinder_hole_radius1 ** 2 + cylinder_hole_radius2 ** 2) + cylinder_height ** 2)
    iyy = (1./12.)*weight*(3*(cylinder_hole_radius1 ** 2 + cylinder_hole_radius2 ** 2) + cylinder_height ** 2)
    izz = (1./2.)*weight*(cylinder_hole_radius1 ** 2 + cylinder_hole_radius2 ** 2)
    gen_inertia(ixx,iyy,izz)

def long_sphere():
    print(long_sphere_a,long_sphere_b,long_sphere_c)
    ixx = (1./5.)*weight*(long_sphere_b ** 2 + long_sphere_c ** 2)
    iyy = (1./5.)*weight*(long_sphere_a ** 2 + long_sphere_c ** 2)
    izz = (1./5.)*weight*(long_sphere_a ** 2 + long_sphere_b ** 2)
    gen_inertia(ixx,iyy,izz)

def cylinder():
    print(cylinder_height,cylinder_radius)
    ixx = (1./12.)*weight*(3*cylinder_radius ** 2 + cylinder_height ** 2)
    iyy = (1./12.)*weight*(3*cylinder_radius ** 2 + cylinder_height ** 2)
    izz = (1./2.)*weight*cylinder_radius ** 2
    gen_inertia(ixx,iyy,izz)

def box():
    print(box_width,box_height,box_depth)
    ixx = (1./12.)*weight*(box_height ** 2  + box_depth ** 2)
    iyy = (1./12.)*weight*(box_width ** 2  + box_depth ** 2)
    izz = (1./12.)*weight*(box_width ** 2  + box_height ** 2)
    gen_inertia(ixx,iyy,izz)


input_dialog_size = (12,20)
key_dict = {"bar_side" : bar_side ,"circular_cone" : circular_cone ,"empty_sphere" : empty_sphere ,"bar_center" : bar_center ,"sphere" : sphere ,"hole_cylinder" : hole_cylinder ,"long_sphere" : long_sphere ,"cylinder" : cylinder ,"box" : box}
layout = [
    [sg.Text("重さ(weight) weight")],
    [sg.Text("weight(kg):"),sg.InputText('0',input_dialog_size)],
    [sg.Text("\n棒(bar) length radius")],
    [sg.Text("length(m):"),sg.InputText('0',input_dialog_size),sg.Text("radius(m):"),sg.InputText('0',input_dialog_size)],
    [sg.Button(key="bar_side",image_size=(200,200),image_filename="imgs/200px-Moment_of_inertia_rod_end.svg.png"),sg.Button(key="bar_center",image_size=(200,200),image_subsample=2,image_filename="imgs/360px-Moment_of_inertia_rod_center.svg.png")],
    [sg.Text("球(sphere) radius")],
    [sg.Text("radius(m):"),sg.InputText('0',input_dialog_size)],
    [sg.Button(key="empty_sphere",image_size=(200,200),image_subsample=2,image_filename="imgs/360px-Moment_of_inertia_hollow_sphere.svg.png"),sg.Button(key="sphere",image_size=(200,200),image_subsample=2,image_filename="imgs/360px-Moment_of_inertia_solid_sphere.svg.png")],
    [sg.Text("長球(long sphere) radius_a radius_b radius_c")],
    [sg.Text("radius_a(m):"),sg.InputText('0',input_dialog_size),sg.Text("radius_b(m):"),sg.InputText('0',input_dialog_size),sg.Text("radius_c(m):"),sg.InputText('0',input_dialog_size)],
    [sg.Button(key="long_sphere",image_size=(200,200),image_subsample=2,image_filename="imgs/360px-Solid_ellipsoid.svg.png")],
    [sg.Text("円柱(cylinder) radius (筒の場合:radius_1 radius_2) height")],
    [sg.Text("radius(m):"),sg.InputText('0',input_dialog_size),sg.Text("radius_1(m):"),sg.InputText('0',input_dialog_size),sg.Text("radius_2(m):"),sg.InputText('0',input_dialog_size),sg.Text("height(m):"),sg.InputText('0',input_dialog_size)],
    [sg.Button(key="cylinder",image_size=(200,200),image_subsample=2,image_filename="imgs/Moment_of_inertia_solid_cylinder.svg.png"),sg.Button(key="hole_cylinder",image_size=(200,200),image_subsample=2,image_filename="imgs/360px-Moment_of_inertia_thick_cylinder_h.svg.png")],
    [sg.Text("箱(box)) width height depth"),sg.Text("円錐(circular cone) radius height",pad=((800,0),(0,0)))],
    [sg.Text("width(m):"),sg.InputText('0',input_dialog_size),sg.Text("height(m):"),sg.InputText('0',input_dialog_size),sg.Text("depth(m):"),sg.InputText('0',input_dialog_size),sg.Text("radius(m):",pad=((200,0),(0,0))),sg.InputText('0',input_dialog_size),sg.Text("height(m):"),sg.InputText('0',input_dialog_size)],
    [sg.Button(key="box",image_size=(200,200),image_filename="imgs/Moment_of_inertia_solid_rectangular_prism.png"),sg.Button(pad=((1000,0),(0,0)),key="circular_cone",image_size=(200,200),image_subsample=2,image_filename="imgs/360px-Moment_of_inertia_cone.svg.png")],
]

window = sg.Window("inertia calc tool GUI", layout)

while True:
   event, value = window.read()
   
   if event in ("Quit", None):
       break
   # 発生したイベントが関数を書いた辞書にあるか調べる
   if event in key_dict:
       get_params(value)
       func_to_call = key_dict[event]
       func_to_call()
   else:
       print("Event {} not in dispatch dictionary".format(event))

window.close()
