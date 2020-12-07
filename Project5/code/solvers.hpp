#ifndef SOLVERS_HPP
#define SOLVERS_HPP


struct Solvers {
    // Here we define common stuff
    int Nx, Nt;
    double dt, t, dx, L, alpha;
    double *u;
    std::string ResOutFileName;
    std::ofile ResOutFile;
    void WriteToFile(std::string fname);
};

class ForwardEuler : public Solvers{
    // Forward Euler solver class
    private:
    protected:
    public:
        void Initialize(int num_int_points, int num_time_points, float dtimestep);
        void CalcOneStep(int j);
        ~ForwardEuler();
};

class BackwardEuler : public Solvers {
    // Backward Euler solver class
    private:
    public:
        BackwardEuler(int num_int_points, int num_time_points, float dtimestep);
};

class CrankNicolson : public Solvers {
    // Crank-Nicolson solver class
    private:
    public:
};

#endif //SOLVERS_HP
