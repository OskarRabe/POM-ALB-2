# SALBP-2 with worker restrictions
This repository contains the implementation of the SALBP-2 with worker restrictions for the course *Research Seminar: Operations Management using Python and Gurobi* taught by Prof. Dr. Thomas Volling at the TU Berlin. It utilizes Python and Gurobi as a solver.

## Data
Our data can be found in the `data` folder. There is a documentation for the `.alb` file format under the `documentation` folder that contains both the original documentation and the additions we made.
Under the `final_data` folder, you can find the final datasets we used for our computations; for low, medium and high order strength. Addtional scripts for calculating the order strength for a given dataset and to calculate a normal distribution of operation multipliers can be found in the `scripts` folder in the root of the repo.
The `final_data` folder additionally contains the original data instances we utilized ($n=20$) as well as the original data, but trimmed to 12 operations.

## Results
### How to execute the code yourself
1. Install the required packages by running `pip install -r requirements.txt`.
2. Open the `alb-2-model.ipynb` Jupyter notebook file.
3. Adjust the `file_path` variable to the dataset you want to use.
4. Run the notebook.

### How to visualize the results
Running the notebook will write an output file in the `output` folder. You can use the `output_visualization.ipynb` notebook to visualize the results. This also allows for visualizing a diagram with multiple pareto fronts for different scenarios.

### Our results
Our results can be found in the `results_raw` folder. You can use them in combinatio with the `output_visualization.ipynb` notebook to visualize the results yourself and explore our data further. See `results-scenarios.ipynb` for a summary of cycle time and smoothness score trade-offs per scenario for all order strengths.