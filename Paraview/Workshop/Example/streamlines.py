# state file generated using paraview version 5.10.0

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1423, 791]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.0, 0.0, 0.07999992370605469]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [38.386555388442, -14.14479390449499, -5.970947294965941]
renderView1.CameraFocalPoint = [0.0, 0.0, 0.07999992370605469]
renderView1.CameraViewUp = [-0.30759220138040255, -0.9268455013975778, 0.21527762119883814]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 12.951115722667065
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1423, 791)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'IOSS Reader'
disk_out_refex2 = IOSSReader(registrationName='disk_out_ref.ex2', FileName=['C:\\Users\\mitja\\Documents\\notes\\Paraview\\Workshop\\Data\\disk_out_ref.ex2'])
disk_out_refex2.ElementBlocks = ['block_1']
disk_out_refex2.NodeBlockFields = ['ash3', 'ch4', 'game3', 'h2', 'pres', 'temp', 'v']
disk_out_refex2.NodeSets = []
disk_out_refex2.SideSets = []

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=disk_out_refex2)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'ash3']
clip1.Value = 0.13265814632177353

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.0, 0.0, 0.07999992370605469]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [0.0, 0.0, 0.07999992370605469]

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=disk_out_refex2)
contour1.ContourBy = ['POINTS', 'temp']
contour1.Isosurfaces = [293.15, 448.15, 603.15, 758.15, 913.15]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Clip'
clip2 = Clip(registrationName='Clip2', Input=contour1)
clip2.ClipType = 'Plane'
clip2.HyperTreeGridClipper = 'Plane'
clip2.Scalars = ['POINTS', 'temp']
clip2.Value = 603.15

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [0.0, 0.0, -0.3867756855615889]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip2.HyperTreeGridClipper.Origin = [0.0, 0.0, -0.3867756855615889]

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=disk_out_refex2,
    SeedType='Line')
streamTracer1.Vectors = ['POINTS', 'v']
streamTracer1.MaximumStreamlineLength = 20.15999984741211

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-5.75, -5.75, -10.0]
streamTracer1.SeedType.Point2 = [5.75, 5.75, 10.15999984741211]
streamTracer1.SeedType.Resolution = 150

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'v'
vLUT = GetColorTransferFunction('v')
vLUT.RGBPoints = [0.0, 0.267004, 0.004874, 0.329415, 0.0879266126953872, 0.26851, 0.009605, 0.335427, 0.17583080657060726, 0.269944, 0.014625, 0.341379, 0.26375741926599444, 0.271305, 0.019942, 0.347269, 0.3516616131412145, 0.272594, 0.025563, 0.353093, 0.43958822583660173, 0.273809, 0.031497, 0.358853, 0.5274924197118218, 0.274952, 0.037752, 0.364543, 0.615419032407209, 0.276022, 0.044167, 0.370164, 0.7033456451025961, 0.277018, 0.050344, 0.375715, 0.7912498389778163, 0.277941, 0.056324, 0.381191, 0.8791764516732035, 0.278791, 0.062145, 0.386592, 0.9670806455484237, 0.279566, 0.067836, 0.391917, 1.0550072582438106, 0.280267, 0.073417, 0.397163, 1.142911452119031, 0.280894, 0.078907, 0.402329, 1.230838064814418, 0.281446, 0.08432, 0.407414, 1.3187646775098052, 0.281924, 0.089666, 0.412415, 1.4066688713850253, 0.282327, 0.094955, 0.417331, 1.4945954840804125, 0.282656, 0.100196, 0.42216, 1.5824996779556326, 0.28291, 0.105393, 0.426902, 1.6704262906510199, 0.283091, 0.110553, 0.431554, 1.75833048452624, 0.283197, 0.11568, 0.436115, 1.846257097221627, 0.283229, 0.120777, 0.440584, 1.9341837099170143, 0.283187, 0.125848, 0.44496, 2.0220879037922344, 0.283072, 0.130895, 0.449241, 2.110014516487621, 0.282884, 0.13592, 0.453427, 2.1979187103628415, 0.282623, 0.140926, 0.457517, 2.2858453230582287, 0.28229, 0.145912, 0.46151, 2.373749516933449, 0.281887, 0.150881, 0.465405, 2.461676129628836, 0.281412, 0.155834, 0.469201, 2.549580323504056, 0.280868, 0.160771, 0.472899, 2.6375069361994434, 0.280255, 0.165693, 0.476498, 2.7254335488948302, 0.279574, 0.170599, 0.479997, 2.8133377427700506, 0.278826, 0.17549, 0.483397, 2.901264355465438, 0.278012, 0.180367, 0.486697, 2.989168549340658, 0.277134, 0.185228, 0.489898, 3.077095162036045, 0.276194, 0.190074, 0.493001, 3.1649993559112652, 0.275191, 0.194905, 0.496005, 3.2529259686066525, 0.274128, 0.199721, 0.498911, 3.3408525813020398, 0.273006, 0.20452, 0.501721, 3.4287567751772596, 0.271828, 0.209303, 0.504434, 3.516683387872647, 0.270595, 0.214069, 0.507052, 3.604587581747867, 0.269308, 0.218818, 0.509577, 3.692514194443254, 0.267968, 0.223549, 0.512008, 3.7804183883184743, 0.26658, 0.228262, 0.514349, 3.8683450010138616, 0.265145, 0.232956, 0.516599, 3.9562716137092484, 0.263663, 0.237631, 0.518762, 4.044175807584469, 0.262138, 0.242286, 0.520837, 4.132102420279856, 0.260571, 0.246922, 0.522828, 4.220006614155076, 0.258965, 0.251537, 0.524736, 4.307933226850463, 0.257322, 0.25613, 0.526563, 4.395837420725683, 0.255645, 0.260703, 0.528312, 4.48376403342107, 0.253935, 0.265254, 0.529983, 4.5716906461164575, 0.252194, 0.269783, 0.531579, 4.659594839991677, 0.250425, 0.27429, 0.533103, 4.7475214526870655, 0.248629, 0.278775, 0.534556, 4.8354256465622845, 0.246811, 0.283237, 0.535941, 4.923352259257672, 0.244972, 0.287675, 0.53726, 5.0112564531328925, 0.243113, 0.292092, 0.538516, 5.099183065828279, 0.241237, 0.296485, 0.539709, 5.187109678523666, 0.239346, 0.300855, 0.540844, 5.275013872398887, 0.237441, 0.305202, 0.541921, 5.362940485094274, 0.235526, 0.309527, 0.542944, 5.450844678969494, 0.233603, 0.313828, 0.543914, 5.538771291664881, 0.231674, 0.318106, 0.544834, 5.626675485540101, 0.229739, 0.322361, 0.545706, 5.714602098235489, 0.227802, 0.326594, 0.546532, 5.802528710930876, 0.225863, 0.330805, 0.547314, 5.8904329048060955, 0.223925, 0.334994, 0.548053, 5.978359517501483, 0.221989, 0.339161, 0.548752, 6.066263711376703, 0.220057, 0.343307, 0.549413, 6.15419032407209, 0.21813, 0.347432, 0.550038, 6.24209451794731, 0.21621, 0.351535, 0.550627, 6.330021130642698, 0.214298, 0.355619, 0.551184, 6.417947743338084, 0.212395, 0.359683, 0.55171, 6.505851937213305, 0.210503, 0.363727, 0.552206, 6.593778549908691, 0.208623, 0.367752, 0.552675, 6.681682743783912, 0.206756, 0.371758, 0.553117, 6.7696093564792985, 0.204903, 0.375746, 0.553533, 6.857513550354519, 0.203063, 0.379716, 0.553925, 6.945440163049907, 0.201239, 0.38367, 0.554294, 7.033344356925126, 0.19943, 0.387607, 0.554642, 7.121270969620514, 0.197636, 0.391528, 0.554969, 7.209197582315901, 0.19586, 0.395433, 0.555276, 7.297101776191121, 0.1941, 0.399323, 0.555565, 7.385028388886508, 0.192357, 0.403199, 0.555836, 7.472932582761728, 0.190631, 0.407061, 0.556089, 7.560859195457116, 0.188923, 0.41091, 0.556326, 7.648763389332335, 0.187231, 0.414746, 0.556547, 7.736690002027723, 0.185556, 0.41857, 0.556753, 7.8246166147231095, 0.183898, 0.422383, 0.556944, 7.91252080859833, 0.182256, 0.426184, 0.55712, 8.000447421293718, 0.180629, 0.429975, 0.557282, 8.088351615168937, 0.179019, 0.433756, 0.55743, 8.176278227864325, 0.177423, 0.437527, 0.557565, 8.264182421739545, 0.175841, 0.44129, 0.557685, 8.352109034434932, 0.174274, 0.445044, 0.557792, 8.440035647130319, 0.172719, 0.448791, 0.557885, 8.527939841005539, 0.171176, 0.45253, 0.557965, 8.615866453700926, 0.169646, 0.456262, 0.55803, 8.703770647576146, 0.168126, 0.459988, 0.558082, 8.791697260271533, 0.166617, 0.463708, 0.558119, 8.879601454146753, 0.165117, 0.467423, 0.558141, 8.96752806684214, 0.163625, 0.471133, 0.558148, 9.055454679537528, 0.162142, 0.474838, 0.55814, 9.143358873412748, 0.160665, 0.47854, 0.558115, 9.231285486108135, 0.159194, 0.482237, 0.558073, 9.319189679983355, 0.157729, 0.485932, 0.558013, 9.407116292678742, 0.15627, 0.489624, 0.557936, 9.495020486553962, 0.154815, 0.493313, 0.55784, 9.58294709924935, 0.153364, 0.497, 0.557724, 9.670873711944736, 0.151918, 0.500685, 0.557587, 9.758777905819958, 0.150476, 0.504369, 0.55743, 9.846704518515343, 0.149039, 0.508051, 0.55725, 9.934608712390565, 0.147607, 0.511733, 0.557049, 10.02253532508595, 0.14618, 0.515413, 0.556823, 10.110439518961172, 0.144759, 0.519093, 0.556572, 10.198366131656558, 0.143343, 0.522773, 0.556295, 10.286292744351947, 0.141935, 0.526453, 0.555991, 10.374196938227167, 0.140536, 0.530132, 0.555659, 10.462123550922554, 0.139147, 0.533812, 0.555298, 10.550027744797774, 0.13777, 0.537492, 0.554906, 10.637954357493161, 0.136408, 0.541173, 0.554483, 10.72585855136838, 0.135066, 0.544853, 0.554029, 10.813785164063768, 0.133743, 0.548535, 0.553541, 10.901711776759155, 0.132444, 0.552216, 0.553018, 10.989615970634375, 0.131172, 0.555899, 0.552459, 11.077542583329762, 0.129933, 0.559582, 0.551864, 11.165446777204982, 0.128729, 0.563265, 0.551229, 11.25337338990037, 0.127568, 0.566949, 0.550556, 11.341277583775591, 0.126453, 0.570633, 0.549841, 11.429204196470979, 0.125394, 0.574318, 0.549086, 11.517108390346197, 0.124395, 0.578002, 0.548287, 11.605035003041584, 0.123463, 0.581687, 0.547445, 11.69296161573697, 0.122606, 0.585371, 0.546557, 11.780865809612191, 0.121831, 0.589055, 0.545623, 11.868792422307578, 0.121148, 0.592739, 0.544641, 11.956696616182798, 0.120565, 0.596422, 0.543611, 12.044623228878187, 0.120092, 0.600104, 0.54253, 12.132527422753405, 0.119738, 0.603785, 0.5414, 12.220454035448792, 0.119512, 0.607464, 0.540218, 12.30838064814418, 0.119423, 0.611141, 0.538982, 12.396284842019401, 0.119483, 0.614817, 0.537692, 12.484211454714787, 0.119699, 0.61849, 0.536347, 12.572115648590007, 0.120081, 0.622161, 0.534946, 12.660042261285396, 0.120638, 0.625828, 0.533488, 12.747946455160616, 0.12138, 0.629492, 0.531973, 12.835873067856001, 0.122312, 0.633153, 0.530398, 12.923799680551388, 0.123444, 0.636809, 0.528763, 13.01170387442661, 0.12478, 0.640461, 0.527068, 13.099630487121997, 0.126326, 0.644107, 0.525311, 13.187534680997215, 0.128087, 0.647749, 0.523491, 13.275461293692604, 0.130067, 0.651384, 0.521608, 13.363365487567824, 0.132268, 0.655014, 0.519661, 13.451292100263212, 0.134692, 0.658636, 0.517649, 13.539218712958597, 0.137339, 0.662252, 0.515571, 13.627122906833819, 0.14021, 0.665859, 0.513427, 13.715049519529206, 0.143303, 0.669459, 0.511215, 13.802953713404424, 0.146616, 0.67305, 0.508936, 13.890880326099815, 0.150148, 0.676631, 0.506589, 13.978784519975033, 0.153894, 0.680203, 0.504172, 14.06671113267042, 0.157851, 0.683765, 0.501686, 14.154637745365806, 0.162016, 0.687316, 0.499129, 14.242541939241027, 0.166383, 0.690856, 0.496502, 14.330468551936415, 0.170948, 0.694384, 0.493803, 14.418372745811634, 0.175707, 0.6979, 0.491033, 14.506299358507023, 0.180653, 0.701402, 0.488189, 14.594203552382242, 0.185783, 0.704891, 0.485273, 14.682130165077629, 0.19109, 0.708366, 0.482284, 14.770056777773016, 0.196571, 0.711827, 0.479221, 14.857960971648238, 0.202219, 0.715272, 0.476084, 14.945887584343623, 0.20803, 0.718701, 0.472873, 15.033791778218843, 0.214, 0.722114, 0.469588, 15.121718390914232, 0.220124, 0.725509, 0.466226, 15.209622584789452, 0.226397, 0.728888, 0.462789, 15.297549197484837, 0.232815, 0.732247, 0.459277, 15.385475810180225, 0.239374, 0.735588, 0.455688, 15.473380004055446, 0.24607, 0.73891, 0.452024, 15.561306616750834, 0.252899, 0.742211, 0.448284, 15.649210810626052, 0.259857, 0.745492, 0.444467, 15.737137423321439, 0.266941, 0.748751, 0.440573, 15.82504161719666, 0.274149, 0.751988, 0.436601, 15.912968229892048, 0.281477, 0.755203, 0.432552, 16.00087242376727, 0.288921, 0.758394, 0.428426, 16.088799036462657, 0.296479, 0.761561, 0.424223, 16.17672564915804, 0.304148, 0.764704, 0.419943, 16.264629843033262, 0.311925, 0.767822, 0.415586, 16.35255645572865, 0.319809, 0.770914, 0.411152, 16.44046064960387, 0.327796, 0.77398, 0.40664, 16.528387262299255, 0.335885, 0.777018, 0.402049, 16.616291456174476, 0.344074, 0.780029, 0.397381, 16.704218068869864, 0.35236, 0.783011, 0.392636, 16.79214468156525, 0.360741, 0.785964, 0.387814, 16.88004887544047, 0.369214, 0.788888, 0.382914, 16.967975488135856, 0.377779, 0.791781, 0.377939, 17.055879682011078, 0.386433, 0.794644, 0.372886, 17.143806294706465, 0.395174, 0.797475, 0.367757, 17.231710488581683, 0.404001, 0.800275, 0.362552, 17.319637101277074, 0.412913, 0.803041, 0.357269, 17.40756371397246, 0.421908, 0.805774, 0.35191, 17.49546790784768, 0.430983, 0.808473, 0.346476, 17.583394520543067, 0.440137, 0.811138, 0.340967, 17.67129871441829, 0.449368, 0.813768, 0.335384, 17.759225327113676, 0.458674, 0.816363, 0.329727, 17.847129520988894, 0.468053, 0.818921, 0.323998, 17.93505613368428, 0.477504, 0.821444, 0.318195, 18.022982746379668, 0.487026, 0.823929, 0.312321, 18.11088694025489, 0.496615, 0.826376, 0.306377, 18.198813552950273, 0.506271, 0.828786, 0.300362, 18.286717746825495, 0.515992, 0.831158, 0.294279, 18.374644359520882, 0.525776, 0.833491, 0.288127, 18.462548553396104, 0.535621, 0.835785, 0.281908, 18.55047516609149, 0.545524, 0.838039, 0.275626, 18.63840177878688, 0.555484, 0.840254, 0.269281, 18.726305972662097, 0.565498, 0.84243, 0.262877, 18.814232585357484, 0.575563, 0.844566, 0.256415, 18.902136779232706, 0.585678, 0.846661, 0.249897, 18.990063391928093, 0.595839, 0.848717, 0.243329, 19.07796758580331, 0.606045, 0.850733, 0.236712, 19.1658941984987, 0.616293, 0.852709, 0.230052, 19.25382081119409, 0.626579, 0.854645, 0.223353, 19.341725005069307, 0.636902, 0.856542, 0.21662, 19.429651617764694, 0.647257, 0.8584, 0.209861, 19.517555811639916, 0.657642, 0.860219, 0.203082, 19.605482424335303, 0.668054, 0.861999, 0.196293, 19.69338661821052, 0.678489, 0.863742, 0.189503, 19.78131323090591, 0.688944, 0.865448, 0.182725, 19.869239843601296, 0.699415, 0.867117, 0.175971, 19.957144037476514, 0.709898, 0.868751, 0.169257, 20.0450706501719, 0.720391, 0.87035, 0.162603, 20.132974844047123, 0.730889, 0.871916, 0.156029, 20.22090145674251, 0.741388, 0.873449, 0.149561, 20.308805650617728, 0.751884, 0.874951, 0.143228, 20.396732263313115, 0.762373, 0.876424, 0.137064, 20.484636457188337, 0.772852, 0.877868, 0.131109, 20.572563069883724, 0.783315, 0.879285, 0.125405, 20.66048968257911, 0.79376, 0.880678, 0.120005, 20.748393876454333, 0.804182, 0.882046, 0.114965, 20.83632048914972, 0.814576, 0.883393, 0.110347, 20.92422468302494, 0.82494, 0.88472, 0.106217, 21.012151295720326, 0.83527, 0.886029, 0.102646, 21.100055489595547, 0.845561, 0.887322, 0.099702, 21.187982102290935, 0.85581, 0.888601, 0.097452, 21.275908714986322, 0.866013, 0.889868, 0.095953, 21.363812908861544, 0.876168, 0.891125, 0.09525, 21.451739521556927, 0.886271, 0.892374, 0.095374, 21.53964371543215, 0.89632, 0.893616, 0.096335, 21.627570328127536, 0.906311, 0.894855, 0.098125, 21.715474522002758, 0.916242, 0.896091, 0.100717, 21.80340113469814, 0.926106, 0.89733, 0.104071, 21.89132774739353, 0.935904, 0.89857, 0.108131, 21.97923194126875, 0.945636, 0.899815, 0.112838, 22.067158553964138, 0.9553, 0.901065, 0.118128, 22.155062747839356, 0.964894, 0.902323, 0.123941, 22.242989360534743, 0.974417, 0.90359, 0.130215, 22.330893554409965, 0.983868, 0.904867, 0.136897, 22.418820167105352, 0.993248, 0.906157, 0.143936]
vLUT.NanColor = [1.0, 0.0, 0.0]
vLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = ['POINTS', 'v']
streamTracer1Display.LookupTable = vLUT
streamTracer1Display.LineWidth = 10.0
streamTracer1Display.RenderLinesAsTubes = 1
streamTracer1Display.SelectTCoordArray = 'None'
streamTracer1Display.SelectNormalArray = 'None'
streamTracer1Display.SelectTangentArray = 'None'
streamTracer1Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.ScaleFactor = 2.015567970275879
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.GaussianRadius = 0.10077839851379394
streamTracer1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [-2.954882363835013, 0.0, 0.5, 0.0, 40.133051371872924, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [-2.954882363835013, 0.0, 0.5, 0.0, 40.133051371872924, 1.0, 0.5, 0.0]

# show data from clip1
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Wireframe'
clip1Display.ColorArrayName = [None, '']
clip1Display.Opacity = 0.5
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'ash3'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 2.015999984741211
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 0.10079999923706055
clip1Display.SetScaleArray = ['POINTS', 'ash3']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'ash3']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityUnitDistance = 1.5409774217348384
clip1Display.OpacityArrayName = ['POINTS', 'ash3']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [0.08047682046890259, 0.0, 0.5, 0.0, 0.18483947217464447, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [0.08047682046890259, 0.0, 0.5, 0.0, 0.18483947217464447, 1.0, 0.5, 0.0]

# show data from clip2
clip2Display = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'temp'
tempLUT = GetColorTransferFunction('temp')
tempLUT.EnableOpacityMapping = 1
tempLUT.RGBPoints = [293.1499938964844, 0.23137254902, 0.298039215686, 0.752941176471, 603.2125091552734, 0.865, 0.865, 0.865, 913.2750244140625, 0.705882352941, 0.0156862745098, 0.149019607843]
tempLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'temp'
tempPWF = GetOpacityTransferFunction('temp')
tempPWF.Points = [293.14999389648455, 0.0, 0.5, 0.0, 913.2750244140623, 1.0, 0.5, 0.0]
tempPWF.UseLogScale = 1
tempPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
clip2Display.Representation = 'Surface'
clip2Display.ColorArrayName = ['POINTS', 'temp']
clip2Display.LookupTable = tempLUT
clip2Display.SelectTCoordArray = 'None'
clip2Display.SelectNormalArray = 'Normals'
clip2Display.SelectTangentArray = 'None'
clip2Display.OSPRayScaleArray = 'temp'
clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display.SelectOrientationVectors = 'None'
clip2Display.ScaleFactor = 1.9226448628876824
clip2Display.SelectScaleArray = 'temp'
clip2Display.GlyphType = 'Arrow'
clip2Display.GlyphTableIndexArray = 'temp'
clip2Display.GaussianRadius = 0.09613224314438412
clip2Display.SetScaleArray = ['POINTS', 'temp']
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityArray = ['POINTS', 'temp']
clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display.DataAxesGrid = 'GridAxesRepresentation'
clip2Display.PolarAxes = 'PolarAxesRepresentation'
clip2Display.ScalarOpacityFunction = tempPWF
clip2Display.ScalarOpacityUnitDistance = 2.103198956817895
clip2Display.OpacityArrayName = ['POINTS', 'temp']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip2Display.ScaleTransferFunction.Points = [293.15, 0.0, 0.5, 0.0, 913.15, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip2Display.OpacityTransferFunction.Points = [293.15, 0.0, 0.5, 0.0, 913.15, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for tempLUT in view renderView1
tempLUTColorBar = GetScalarBar(tempLUT, renderView1)
tempLUTColorBar.WindowLocation = 'Any Location'
tempLUTColorBar.Position = [0.8897082004617882, 0.504424778761062]
tempLUTColorBar.Title = 'temp'
tempLUTColorBar.ComponentTitle = ''
tempLUTColorBar.ScalarBarLength = 0.32999999999999985

# set color bar visibility
tempLUTColorBar.Visibility = 1

# get color legend/bar for vLUT in view renderView1
vLUTColorBar = GetScalarBar(vLUT, renderView1)
vLUTColorBar.WindowLocation = 'Any Location'
vLUTColorBar.Position = [0.8801529470289534, 0.0960809102402023]
vLUTColorBar.Title = 'v'
vLUTColorBar.ComponentTitle = 'Magnitude'
vLUTColorBar.ScalarBarLength = 0.32999999999999996

# set color bar visibility
vLUTColorBar.Visibility = 1

# show color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'v'
vPWF = GetOpacityTransferFunction('v')
vPWF.Points = [0.0, 0.0, 0.5, 0.0, 22.418820167105352, 1.0, 0.5, 0.0]
vPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(streamTracer1)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')