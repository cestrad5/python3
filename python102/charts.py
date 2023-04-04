import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


if __name__ == '__main__':
    labels = ['aas', 'basf', 'cadf']
    values = [10,20,18]
    generate_bar_chart(labels, values)