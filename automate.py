try:
    import graphviz
except ImportError:
    import os
    os.system('pip install graphviz')
    import graphviz

def draw_automaton():
    dot = graphviz.Digraph(format="png")
    
    dot.attr(rankdir="LR")  # Disposition horizontale
    dot.node("q0", "q0 (initial, final)", shape="doublecircle")
    dot.node("q1", "q1", shape="circle")
    
    dot.edge("q0", "q1", label="a")
    dot.edge("q1", "q0", label="b")
    
    return dot

if __name__ == "__main__":
    automate = draw_automaton()
    output_path = "automate_ab_star"
    automate.render(output_path, format="png", cleanup=True)
    print(f"Automate généré : {output_path}.png")

