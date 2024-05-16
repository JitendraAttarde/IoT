try:
    print(var)
except Exception as e:
    print(f"Erro has come : {e}")
#except NameError:
#    print("Variable is not declared")
except:
    print("Error has come")