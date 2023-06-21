

def vowel_count(words: list):
    """
        Conta o número de vogais em cada palavra de uma lista fornecida e retorna um dicionário
        com a palavra como chave e a contagem como valor.

        Args:
            words (list): Lista de palavras para contar as vogais.
        Returns:
            dict: Um dicionário com a palavra como chave e o número de vogais como valor.
        """
    result = {}
    for word in words:
        vowels = [char for char in word if char.lower() in 'aeiou']
        result[word] = len(vowels)
    return result


def sort_words(words: list, order: str):
    """
       Ordena uma lista de palavras em ordem ascendente ou descendente com base na ordem fornecida.

       Args:
           words (list): Lista de palavras a serem ordenadas.
           order (str): Ordem para ordenar as palavras. Os valores válidos são 'asc' para ascendente
           e 'desc' para descendente.

       Returns:
           list: A lista de palavras ordenada.
       """
    return words[::-1] if order == 'desc' else words


def validate_words(value):
    """
    Valida o valor fornecido para garantir que seja uma lista de strings.

    Args:
        value: O valor a ser validado.
    Returns:
        list: A lista de strings validada.
    Raises:
        ValueError: Se o valor não for uma lista válida de strings.
    """
    if not isinstance(value, list) or not all(isinstance(word, str) for word in value):
        raise ValueError("Value is not a valid list of strings")
    return value
