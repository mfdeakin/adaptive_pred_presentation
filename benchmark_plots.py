
from matplotlib import pyplot as plt
from numpy import array, arange

tri = array([[8.9206115367857530262796217357390560209751129150390625e-01,
              9.020611536785754136502646360895596444606781005859375e-01,
              2.773088457873296164279963704757392406463623046875e-01,
              8.9206115367857530262796217357390560209751129150390625e-01],
             [9.5046631112696389198646329532493837177753448486328125e-01,
              9.604663111269640030087657578405924141407012939453125e-01,
              -3.756180752683186963025718796416185796260833740234375e-01,
              9.5046631112696389198646329532493837177753448486328125e-01],
             ])

fig, (ax) = plt.subplots(nrows=1)
ax.set_title('3 Point Orientation Test')
plt.plot(tri[0], tri[1], color='red', ls='', marker='o', markersize=5)
plt.plot(tri[0], tri[1], color='black')
plt.text(tri[0][0] * (1 - 0.05), tri[1][0] * (1 + 0.01), 'Pt 0', fontsize=12)
plt.text(tri[0][1] * (1 + 0.01), tri[1][1] * (1 + 0.01), 'Pt 1', fontsize=12)
plt.text(tri[0][2] * (1 + 0.05), tri[1][2] * (1 + 0.05), 'Pt 2', fontsize=12)
plt.show()

confidence_factor = 0.196

fp_no_expr = (1.17467, 0.0125226 * confidence_factor)
fp_expr = (1.18048, 0.232348 * confidence_factor)
exact = (77.3984, 17.6987 * confidence_factor)

x = arange(0.5, 3, 1)
height = array([fp_no_expr[0], fp_expr[0], exact[0]])
errors = array([fp_no_expr[1], fp_expr[1], exact[1]])
labels = ['FP', 'FP Expr', 'Exact']

fig, (ax) = plt.subplots(nrows=1)
ax.set_title('Performance Comparison')
ax.set_ylabel('Time (ns)')
b = ax.bar(x, height, yerr=errors)
ax.set_xticks(x, labels)

adaptive = (14.5915, 1.44975 * confidence_factor)
shewchuk = (2.84544, 0.0427542 * confidence_factor)
cgal = (6.27468, 0.228188 * confidence_factor)
height = array([fp_no_expr[0], exact[0], adaptive[0], shewchuk[0], cgal[0]])
errors = array([fp_no_expr[1], exact[1], adaptive[1], shewchuk[1], cgal[1]])

labels = ['FP', 'Exact', 'Adaptive', 'Shewchuk', 'CGAL Exact']

x = arange(0.5, 5, 1)
fig, (ax) = plt.subplots(nrows=1)
ax.set_title('Performance Comparison, only requiring doubles')
ax.set_ylabel('Time (ns)')
b = ax.bar(x, height, yerr=errors)
ax.set_xticks(x, labels)

adaptive = (88.3614, 11.2353 * confidence_factor)
shewchuk = (23.3111, 3.84555 * confidence_factor)
cgal = (146.477, 24.6258 * confidence_factor)
height = array([fp_no_expr[0], exact[0], adaptive[0], shewchuk[0], cgal[0]])
errors = array([fp_no_expr[1], exact[1], adaptive[1], shewchuk[1], cgal[1]])

x = arange(0.5, 5, 1)
fig, (ax) = plt.subplots(nrows=1)
ax.set_title('Performance Comparison, requires adaptation')
ax.set_ylabel('Time (ns)')
b = ax.bar(x, height, yerr=errors)
ax.set_xticks(x, labels)
plt.show()
