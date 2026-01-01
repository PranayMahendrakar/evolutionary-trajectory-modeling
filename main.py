#!/usr/bin/env python3
"""Evolutionary Trajectory Modeling System - Author: Pranay M"""
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.markdown import Markdown
from modules import *

console = Console()

def main():
    console.print(Panel("🧬 EVOLUTIONARY TRAJECTORY MODELING SYSTEM 🧬\nMapping Future Evolution", style="bold green"))
    mods = [("Trajectory Prediction", TrajectoryPredictor()), ("Fitness Landscapes", FitnessLandscapeMapper()),
            ("Selection Pressure", SelectionPressureAnalyzer()), ("Mutation Modeling", MutationModeler()),
            ("Convergence Detection", ConvergenceDetector()), ("Divergence Analysis", DivergenceAnalyzer()),
            ("Extinction Prediction", ExtinctionPredictor()), ("Adaptation Simulation", AdaptationSimulator()),
            ("Intelligence Evolution", IntelligenceEvolver()), ("Synthesis", SynthesisEngine())]
    while True:
        table = Table(title="Evolution Modules")
        for i,(n,_) in enumerate(mods,1): table.add_row(str(i),n)
        table.add_row("0","Exit")
        console.print(table)
        c = Prompt.ask("Select", choices=[str(i) for i in range(len(mods)+1)])
        if c == "0": break
        entity = Prompt.ask("Entity/lineage to model")
        result = mods[int(c)-1][1].model(entity)
        console.print(Panel(Markdown(result), title=mods[int(c)-1][0], border_style="green"))

if __name__ == "__main__": main()
