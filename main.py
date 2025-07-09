import tkinter as tk
import random
import time

# Main window setup
root = tk.Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(1000, 600)
root.config(bg='black')

# Canvas for drawing bars
canvas = tk.Canvas(root, width=980, height=400, bg='white')
canvas.pack(pady=20)

# Draw bars function
def draw_bars(data, colorArray):
    canvas.delete("all")
    c_height = 400
    c_width = 980
    bar_width = c_width / (len(data) + 1)
    spacing = 10

    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * bar_width + spacing
        y0 = c_height - height * 360
        x1 = (i + 1) * bar_width
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(data[i]))

    root.update_idletasks()


# Sorting Algorithms

def bubble_sort(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_bars(data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(data))])
                time.sleep(0.1)
    draw_bars(data, ['blue' for _ in range(len(data))])


def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
            draw_bars(data, ['green' if x == j or x == min_idx else 'red' for x in range(len(data))])
            time.sleep(0.1)
        data[i], data[min_idx] = data[min_idx], data[i]
    draw_bars(data, ['blue' for _ in range(len(data))])


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            draw_bars(data, ['green' if x == j or x == i else 'red' for x in range(len(data))])
            time.sleep(0.1)
        data[j + 1] = key
    draw_bars(data, ['blue' for _ in range(len(data))])


def merge_sort(data, draw, speed):
    def merge_sort_recursive(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_recursive(arr, left, mid)
            merge_sort_recursive(arr, mid + 1, right)
            merge(arr, left, mid, right)

    def merge(arr, left, mid, right):
        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1
            draw_bars(arr, ['green' if x >= left and x <= right else 'red' for x in range(len(arr))])
            time.sleep(speed)

        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1
            draw_bars(arr, ['green' if x >= left and x <= right else 'red' for x in range(len(arr))])
            time.sleep(speed)

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1
            draw_bars(arr, ['green' if x >= left and x <= right else 'red' for x in range(len(arr))])
            time.sleep(speed)

    merge_sort_recursive(data, 0, len(data) - 1)
    draw_bars(data, ['blue' for _ in range(len(data))])


def quick_sort(data, low, high, draw, speed):
    if low < high:
        pivot_index = partition(data, low, high, draw, speed)
        quick_sort(data, low, pivot_index - 1, draw, speed)
        quick_sort(data, pivot_index + 1, high, draw, speed)

def partition(data, low, high, draw, speed):
    pivot = data[high]
    i = low - 1

    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            draw_bars(data, ['green' if x == i or x == j else 'red' for x in range(len(data))])
            time.sleep(speed)
    data[i + 1], data[high] = data[high], data[i + 1]
    draw_bars(data, ['green' if x == i + 1 or x == high else 'red' for x in range(len(data))])
    time.sleep(speed)
    return i + 1


# Dispatcher based on dropdown selection
def start_sorting(data):
    selected_algo = algo_var.get()
    if selected_algo == 'Bubble Sort':
        bubble_sort(data)
    elif selected_algo == 'Selection Sort':
        selection_sort(data)
    elif selected_algo == 'Insertion Sort':
        insertion_sort(data)
    elif selected_algo == 'Merge Sort':
        merge_sort(data, draw_bars, 0.1)
    elif selected_algo == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, draw_bars, 0.1)


# Generate random data
def generate():
    global data
    data = [random.randint(10, 100) for _ in range(25)]
    draw_bars(data, ['red' for _ in range(len(data))])


# UI Frame
btn_frame = tk.Frame(root, bg='black')
btn_frame.pack(pady=10)

# Dropdown menu
algo_var = tk.StringVar()
algo_choices = ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort']
algo_var.set('Bubble Sort')
algo_menu = tk.OptionMenu(btn_frame, algo_var, *algo_choices)
algo_menu.grid(row=0, column=0, padx=10)

# Buttons
tk.Button(btn_frame, text='Generate Data', command=generate, bg='orange').grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text='Start Sorting', command=lambda: start_sorting(data), bg='lightgreen').grid(row=0, column=2, padx=10)

# Start GUI loop
root.mainloop()
