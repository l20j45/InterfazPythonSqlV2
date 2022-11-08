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
p3 AltaContratoCsv1.py  && cat contratossqlTratado.Sql | clip.exe
```

4. Usamos el scritps para comprimirlo ya que esta bien

```bash
 p3 AltaContratoCsv2.py && cat ContratosSqlTratadoZip.sql | clip.exe
```

5. Usamos la alta de abonos 
   
   ```bash
   p3 AltaAbonosV2csv1.py  && cat abonosSqlTratado.Sql | clip.exe
   ```
   
6. Usamos la alta de abonos para comprimirlo ya que esta bien
   
   ```bash
   p3 AltaAbonosV2csv1.py  && cat abonosSqlTratado.Sql | clip.exe
   ```
   
7. Usamos la alta de abonos 
   
   ```bash
   p3 AltaAbonosV2csv1.py  && cat abonosSqlTratado.Sql | clip.exe
   ```

8. Ejecutamos para generar los gestores
   
   ```bash
   p3 AltaGestorContratos.py
   ```
   ```bash
   p3 AltaGestorAbonos.py
   ```

9. truncamos de nuevo 
   
   ```bash
   p3 truncate.py
   ```

10. Juntamos las salidas

   ```bash
   p3 truncate.py
   ```
   ```bash
   p3 truncate.py
   ```
   ```bash
   p3 truncate.py
   ```