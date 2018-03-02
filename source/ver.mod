# Declarations
set V;
set E within V cross V;
set Idx;
set Q within Idx cross V;
set cnt within Idx cross V;

var x {v in V} binary;    # integrality constraints.

# Objective Function
minimize cover_size: sum { v in V } x[v];

# Constraints
subject to clique {c in Idx}: 
    sum {(a, b) in Q: a = c} x[b] >= card{(a,b) in Q: a = c} -1;

data ver.dat;
option solver cplexamp;

solve;

# Output
printf  {u in V : x[u] >= 1}: "%d \n", u > output.out;
end;
