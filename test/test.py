# %%

class Test():
    def __init__(self):
        self.test_import()
        self.test_data()
        self.test_plot()

    def test_import(self):
        import pastamarkers
        from pastamarkers import markers

        print("imported")

    def test_data(self):
        import os
        import pastamarkers

        print(pastamarkers.dir_data)
        print(os.path.dirname(pastamarkers.__file__))
    
    def test_plot(self):

        import pastamarkers
        from pastamarkers import markers
        import numpy as np
        import matplotlib.pyplot as plt

        dir_data = pastamarkers.dir_data + "MPD/"

        xUV,yUV = np.genfromtxt(dir_data+"UV.csv", delimiter=",", unpack=1)     
        xB,yB = np.genfromtxt(dir_data+"B.csv", delimiter=",", unpack=1)     
        xIR,yIR = np.genfromtxt(dir_data+"IR.csv", delimiter=",", unpack=1)     
        xIR_curve,yIR_curve = np.genfromtxt(dir_data+"IR_curve.csv", delimiter=",", unpack=1)  
        xB_curve,yB_curve = np.genfromtxt(dir_data+"B_curve.csv", delimiter=",", unpack=1)  
        xUV_curve,yUV_curve = np.genfromtxt(dir_data+"UV_curve.csv", delimiter=",", unpack=1)  
        fig, ax = plt.subplots(dpi=300, figsize=(5,4))
        ax.scatter(xIR, yIR, marker=markers.fusilli2, s=700,  color="darkred", linewidth=0.2, label="IR-band")
        ax.scatter(xB, yB, marker=markers.tortellini, s=300, color="dodgerblue", linewidth=0.2, label="B-band")
        ax.scatter(xUV, yUV, marker=markers.farfalle, s=500, color="purple", linewidth=0.1, label="UV-band")
        ax.plot(xIR_curve,yIR_curve, color="darkred", lw=0.8, ls="--")
        ax.plot(xB_curve,yB_curve, color="dodgerblue", lw=0.8, ls="--")
        ax.plot(xUV_curve,yUV_curve, color="purple", lw=0.8, ls="--")
        plt.legend()
        plt.title("Madau, Pozzetti & Dickinson (1998)")
        plt.xlabel("redshift")
        plt.ylabel(r"$\log \rho_\nu \, (\mathrm{erg \, s^{-1} \, Hz^{-1} \, Mpc^{-3}})$")
        plt.plot()

        plt.tight_layout()
        plt.savefig("test.png")

# %%

if __name__ == "__main__":
    Test()


# %%
