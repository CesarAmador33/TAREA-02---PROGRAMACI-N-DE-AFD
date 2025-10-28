class DFA:
    """
    Clase para modelar un Autómata Finito Determinista (AFD).
    
    M = (Q, Sigma, delta, q0, F)
    """
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        """
        Inicializa el AFD.

        :param states: Conjunto de estados (set o list).
        :param alphabet: Conjunto de símbolos del alfabeto (set o list).
        :param transitions: Diccionario de transiciones: {(estado, simbolo): siguiente_estado}.
        :param start_state: Estado inicial.
        :param accept_states: Conjunto de estados de aceptación (set o list).
        """
        self.Q = set(states)
        self.Sigma = set(alphabet)
        self.delta = transitions
        self.q0 = start_state
        self.F = set(accept_states)
    
    def accepts(self, chain):
        """
        Simula el procesamiento de una cadena por el AFD.

        :param chain: La cadena de entrada (string).
        :return: True si la cadena es aceptada, False en caso contrario.
        """
        current_state = self.q0
        
        # El autómata acepta la cadena vacía si el estado inicial es un estado de aceptación
        if chain == "":
            return current_state in self.F

        # Procesa cada símbolo en la cadena
        for symbol in chain:
            if symbol not in self.Sigma:
                print(f"Error: Símbolo '{symbol}' no pertenece al alfabeto.")
                return False
            
            # Aplica la función de transición
            if (current_state, symbol) in self.delta:
                current_state = self.delta[(current_state, symbol)]
            else:
                # Esto no debería ocurrir en un AFD bien definido (completo),
                # pero es una buena práctica manejar transiciones no definidas.
                print(f"Error: Transición no definida para el estado {current_state} y símbolo {symbol}.")
                return False

        # La cadena es aceptada si el estado final es un estado de aceptación
        return current_state in self.F

# ----------------------------------------------------------------------
## EJERCICIO 1: El Perrito Guardián (Subcadena "aba")
# ----------------------------------------------------------------------

# Q = {q0, q1, q2, q_aba}
# F = {q_aba}
# Transiciones:
# q0 --a--> q1, q0 --b--> q0
# q1 --a--> q1, q1 --b--> q2
# q2 --a--> q_aba, q2 --b--> q0
# q_aba --a--> q_aba, q_aba --b--> q_aba

perrito_guardian = DFA(
    states={'q0', 'q1', 'q2', 'q_aba'},
    alphabet={'a', 'b'},
    transitions={
        ('q0', 'a'): 'q1', ('q0', 'b'): 'q0',
        ('q1', 'a'): 'q1', ('q1', 'b'): 'q2',
        ('q2', 'a'): 'q_aba', ('q2', 'b'): 'q0',
        ('q_aba', 'a'): 'q_aba', ('q_aba', 'b'): 'q_aba',
    },
    start_state='q0',
    accept_states={'q_aba'}
)

# ----------------------------------------------------------------------
## EJERCICIO 2: El Gatito de los Tres Pasos (Longitud Múltiplo de 3)
# ----------------------------------------------------------------------

# Q = {q0, q1, q2} (q_i representa longitud mod 3 = i)
# F = {q0}
# Transiciones:
# q0 --a/b--> q1
# q1 --a/b--> q2
# q2 --a/b--> q0

gatito_tres_pasos = DFA(
    states={'q0', 'q1', 'q2'},
    alphabet={'a', 'b'},
    transitions={
        ('q0', 'a'): 'q1', ('q0', 'b'): 'q1',
        ('q1', 'a'): 'q2', ('q1', 'b'): 'q2',
        ('q2', 'a'): 'q0', ('q2', 'b'): 'q0',
    },
    start_state='q0',
    accept_states={'q0'}
)

# ----------------------------------------------------------------------
## EJERCICIO 3: El Loro que Contaba 'a's Pares (Paridad de 'a's)
# ----------------------------------------------------------------------

# Q = {q_par, q_impar}
# F = {q_par}
# Transiciones:
# q_par --a--> q_impar, q_par --b--> q_par
# q_impar --a--> q_par, q_impar --b--> q_impar

loro_par_as = DFA(
    states={'q_par', 'q_impar'},
    alphabet={'a', 'b'},
    transitions={
        ('q_par', 'a'): 'q_impar', ('q_par', 'b'): 'q_par',
        ('q_impar', 'a'): 'q_par', ('q_impar', 'b'): 'q_impar',
    },
    start_state='q_par',
    accept_states={'q_par'}
)

# ----------------------------------------------------------------------
## EJERCICIO 4: El Conejo que Termina en 'bb'
# ----------------------------------------------------------------------

# Q = {q0, q1, q2}
# F = {q2}
# Transiciones:
# q0 --a--> q0, q0 --b--> q1 (visto b)
# q1 --a--> q0, q1 --b--> q2 (visto bb)
# q2 --a--> q0, q2 --b--> q2 (visto ...b)

conejo_termina_bb = DFA(
    states={'q0', 'q1', 'q2'},
    alphabet={'a', 'b'},
    transitions={
        ('q0', 'a'): 'q0', ('q0', 'b'): 'q1',
        ('q1', 'a'): 'q0', ('q1', 'b'): 'q2',
        ('q2', 'a'): 'q0', ('q2', 'b'): 'q2',
    },
    start_state='q0',
    accept_states={'q2'}
)

# ----------------------------------------------------------------------
## Prueba de los AFDs
# ----------------------------------------------------------------------

def run_tests(dfa, name, accepts_list, rejects_list):
    """Ejecuta y muestra pruebas para un AFD."""
    print(f"\n--- {name} ---")
    
    print("\n✅ Cadenas Aceptadas (TEST POSITIVO):")
    for chain in accepts_list:
        result = dfa.accepts(chain)
        status = "ACEPTADA" if result else "RECHAZADA (FALLO)"
        print(f"  Cadena: '{chain}' \t-> {status}")

    print("\n❌ Cadenas Rechazadas (TEST NEGATIVO):")
    for chain in rejects_list:
        result = dfa.accepts(chain)
        status = "RECHAZADA" if not result else "ACEPTADA (FALLO)"
        print(f"  Cadena: '{chain}' \t-> {status}")

# 1. El Perrito Guardián
run_tests(
    perrito_guardian, "EJERCICIO 1: El Perrito Guardián",
    accepts_list=["aba", "abab", "baba", "aabaa", "abababa", "bababaaaba"],
    rejects_list=["a", "ab", "ba", "aab", "bba", "babbab"]
)

# 2. El Gatito de los Tres Pasos
run_tests(
    gatito_tres_pasos, "EJERCICIO 2: El Gatito de los Tres Pasos",
    accepts_list=["", "aaa", "abb", "aab", "bbbaaa", "babaaa"],
    rejects_list=["a", "ab", "abab", "aaaab", "baba", "bbbbaa"]
)

# 3. El Loro que Contaba 'a's Pares
run_tests(
    loro_par_as, "EJERCICIO 3: El Loro que Contaba 'a's Pares",
    accepts_list=["", "b", "bb", "aa", "abab", "bbaa", "aabb", "bbaabb", "babbab"],
    rejects_list=["a", "ab", "aaa", "bab", "aaab", "aba", "abbba"]
)

# 4. El Conejo que Termina en 'bb'
run_tests(
    conejo_termina_bb, "EJERCICIO 4: El Conejo que Termina en 'bb'",
    accepts_list=["bb", "abb", "aabb", "babb", "ababb", "aabbb", "baabbbabb"],
    rejects_list=["", "a", "b", "ab", "ba", "aba", "bba", "babba"]
)

# Ejecuta este código en un entorno Python para ver la simulación.