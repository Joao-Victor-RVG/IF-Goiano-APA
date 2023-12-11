# Project Documentation

## Introduction

This document describes the project and provides information about the code contained in the files `code.py` and `recorrencytest.py`. The file `code.py` contains implementations of sorting algorithms and a recursive function, while the file `recorrencytest.py` is responsible for analyzing recurrence in the functions of `code.py`.

## `code.py`

### Code Structure

The `code.py` file contains the following sections:

1. **List of Numbers for Analysis:**
   
   ```python
   arr = [1, 5, 6, 2, 8, 3, 9, 7, 10, 12, 4]
   ```

   This list is used as input for the sorting algorithms and the recursive function.

2. **Factorial Function:**

   ```python
   def factorial(n):
       # ...
   ```

   The `factorial` function calculates the factorial of a number.

3. **Binary Search:**

   ```python
   def binary_search(arr, key):
       # ...
   ```

   The `binary_search` function implements the binary search algorithm on a sorted list.

4. **Sorting Algorithms:**

   - Bubble Sort
   - Insertion Sort
   - Quick Sort
   - Merge Sort

   ```python
   def bubble_sort(arr):
       # ...

   def insertion_sort(arr):
       # ...

   def quicksort(arr):
       # ...

   def mergesort(arr):
       # ...
   ```

   Implementations of sorting algorithms.

### Using the Algorithms

- The sorting algorithms (`bubble_sort`, `insertion_sort`, `quicksort`, `mergesort`) can be used by calling the corresponding function and passing the list to be sorted as an argument.

- Example:

  ```python
  bubble_sort(arr)
  print("List sorted by Bubble Sort:", arr)
  ```

- The binary search function can also be used as follows:

  ```python
  result = binary_search(arr, 7)
  if result != -1:
      print("Element found at position:", result)
  else:
      print("Element not found in the list.")
  ```

## `recorrencytest.py`

### Code Structure

The `recorrencytest.py` file contains a `FunctionVisitor` class that uses the `ast` library to analyze recurrence in functions defined in `code.py`. The recurrence analysis is based on counting recursive calls.

### Using Recurrence Analysis

- To perform recurrence analysis, instantiate the `FunctionVisitor` class and call the `analyze_recurrence` method, passing the path of the `code.py` file as an argument.

- Example:

  ```python
  from recorrencytest import analyze_recurrence

  if __name__ == "__main__":
      path = "code.py"
      analyze_recurrence(path)
  ```

- The result of the analysis will be displayed on the console, indicating whether the function is recursive and providing the recurrence expression if found.

## Conclusion

This document provides an overview of the project and guidance on how to use and understand the code in the `code.py` and `recorrencytest.py` files. Make sure to follow the usage instructions and adapt as needed to meet the specific requirements of your project.

<br>


<br>


## Introdução

Este documento descreve o projeto e fornece informações sobre os códigos contidos nos arquivos `code.py` e `recorrencytest.py`. O arquivo `code.py` contém implementações de algoritmos de ordenação e uma função recursiva, enquanto o arquivo `recorrencytest.py` é responsável por analisar a recorrência nas funções do arquivo `code.py`.

## `code.py`

### Estrutura do Código

O arquivo `code.py` contém as seguintes seções:

1. **Lista de Números para Análise:**
   
   ```python
   arr = [1, 5, 6, 2, 8, 3, 9, 7, 10, 12, 4]
   ```

   Esta lista é usada como entrada para os algoritmos de ordenação e para a função recursiva.

2. **Função Fatorial:**

   ```python
   def fatorial(n):
       # ...
   ```

   A função `fatorial` calcula o fatorial de um número.

3. **Busca Binária:**

   ```python
   def busca_binaria(arr, chave):
       # ...
   ```

   A função `busca_binaria` implementa o algoritmo de busca binária em uma lista ordenada.

4. **Algoritmos de Ordenação:**

   - Bubble Sort
   - Insertion Sort
   - Quick Sort
   - Merge Sort

   ```python
   def bubble_sort(arr):
       # ...

   def insertion_sort(arr):
       # ...

   def quicksort(arr):
       # ...

   def mergesort(arr):
       # ...
   ```

   Implementações dos algoritmos de ordenação.

### Uso dos Algoritmos

- Os algoritmos de ordenação (`bubble_sort`, `insertion_sort`, `quicksort`, `mergesort`) podem ser utilizados chamando a função correspondente e passando a lista a ser ordenada como argumento.

- Exemplo:

  ```python
  bubble_sort(arr)
  print("Lista ordenada pelo Bubble Sort:", arr)
  ```

- A função de busca binária também pode ser utilizada da seguinte maneira:

  ```python
  resultado = busca_binaria(arr, 7)
  if resultado != -1:
      print("Elemento encontrado na posição:", resultado)
  else:
      print("Elemento não encontrado na lista.")
  ```

## `recorrencytest.py`

### Estrutura do Código

O arquivo `recorrencytest.py` contém uma classe `FunctionVisitor` que utiliza a biblioteca `ast` para analisar a recorrência nas funções definidas no arquivo `code.py`. A análise de recorrência é baseada na contagem de chamadas recursivas.

### Uso da Análise de Recorrência

- Para realizar a análise de recorrência, é necessário instanciar a classe `FunctionVisitor` e chamar o método `analyze_recurrence` passando o caminho do arquivo `code.py` como argumento.

- Exemplo:

  ```python
  from recorrencytest import analyze_recurrence

  if __name__ == "__main__":
      path = "code.py"
      analyze_recurrence(path)
  ```

- O resultado da análise será exibido no console, indicando se a função é recursiva e fornecendo a expressão de recorrência, caso seja encontrada.

## Conclusão

Este documento fornece uma visão geral do projeto e orientações sobre como usar e entender os códigos nos arquivos `code.py` e `recorrencytest.py`. Certifique-se de seguir as instruções de uso e adapte conforme necessário para atender às necessidades específicas do seu projeto.



