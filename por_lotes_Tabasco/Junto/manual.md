## como usar los scripts para migrar

1. Usar el script de aleatorio de esta manerapython

```bash
p3 aleatorios.py && notepad.exe AleatoriosContratos.txt && notepad.exe AleatoriosAbonos.txt
```

2. Usamos el truncate.py
   
   ```bash
   p3 truncate.py
   ```

3. Usar el script de los contratos 

```bash
p3 AltaContratos.py && cat contratossql.txt | clip.exe
```

4. Usamos la alta de abonos 
   
   ```bash
   p3 AltaAbonos.py && cat abonosSql.txt | clip.exe
   ```

5. juntamos los dos en un archivo sql 
   
   ```bash
   cat contratossql.txt abonosSql.txt > juntos.sql
   ```

6. truncamos de nuevo 
   
   ```bash
   p3 truncate.py
   ```

7. ejecutamos todo el script
   
    cat juntos.sql | clip.exe