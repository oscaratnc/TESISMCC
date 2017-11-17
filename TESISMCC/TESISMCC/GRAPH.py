import matplotlib.pyplot as plt
i=0
red = [221072, 221115, 221160, 286758, 286766, 286772, 286789, 286796, 286793, 286711, 286684, 286691, 286711, 286712, 286727, 286712, 286730, 286723, 286721, 286689, 286637, 286667, 286705, 286719, 286712, 286669, 286692, 286724, 286731, 286734, 286682, 286665, 286702, 286728, 286755, 286754, 286762, 286714, 286755, 286754, 286765, 286764, 286778, 286764, 286779, 286751, 286730, 286730, 286683, 286713, 286698, 286714, 286681, 286688, 286652, 286643, 286632, 286635, 286628, 286588, 286578, 286577, 286595, 286586, 286557, 286585, 286590, 286569, 286564, 286584, 286572, 286551, 286537, 286541, 286559, 286566, 286577, 286573, 286568, 286563, 286480, 286490, 286507, 286535, 286524, 286504, 286504, 286496, 286507, 286435, 286448, 286471, 286492, 286486, 286523, 286530, 286560, 286521, 286468, 286474, 286495, 286490, 286491, 286504, 286515, 286493, 286417, 286438, 286482, 286485, 286486, 286497, 286503, 286493, 286406, 286421, 286460, 286473, 286488, 286507, 286513, 286524, 286428, 286430, 286441, 286462, 286450, 286452, 286468, 286467, 286473, 286428, 286353, 286370, 286403, 286416, 286416, 286447, 286436, 286436, 286318, 286352, 286358, 286374, 286405, 286416, 286424, 286425, 286407, 286314, 286356, 286371, 286375, 286381, 286403, 286405, 286409, 286402, 286311, 286324, 286369, 286380, 286374, 286382, 286383, 286387, 286373, 286308, 286347, 286368, 286356, 286364, 286373, 286370, 286368, 286339, 286294, 286323, 286341, 286350, 286351, 286359, 286368, 286302, 286259, 286267, 286302, 286298, 286314, 286319, 286353, 286357, 286248, 286306, 286282, 286329, 286343, 286350, 286343, 286346, 286354, 286359, 286311, 286310, 286324, 286325, 286323, 286322, 286334, 286327, 286331, 286283, 286300, 286322, 286333, 286334, 286341, 286344, 286327, 286321, 286289, 286311, 286313, 286310, 286321, 286320, 286324, 286310, 286276, 286273, 286289, 286306, 286306, 286307, 286303, 286303, 286307, 286244, 286255, 286269, 286288, 286284, 286279, 286297, 286289, 286293, 286228, 286237, 286259, 286270, 286283, 286285, 286292, 286290, 286283, 286288, 286252, 286257, 286256, 286277, 286274, 286274, 286276, 286274, 286267, 286224, 286253, 286249, 286255, 286271, 286268, 286276, 286275, 286230, 286219, 286215, 286246, 286237, 286252, 286257, 286264, 286266, 286265, 286200, 286221, 286234, 286245, 286245, 286243, 286261, 286266, 286251, 286212, 286223, 286228, 286233, 286243, 286251, 286232]

time = [None]*len(red)

for i in range (len(red)):
    time[i]=i
    
axes = plt.gca()
axes.set_ylim([max(red)-500, max(red)+500])
plt.plot(time,red)

plt.show()
