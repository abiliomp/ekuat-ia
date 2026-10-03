<?php
/**
 * Valida un rDE o un gGroupGesEve contra los XSD de esta carpeta (copias de producción con
 * schemaLocation relativos y el fix de `dEntCont`). Sin red.
 *
 * Uso:  php validar.php documento.xml [documento2.xml ...]
 *       php validar.php --fiel documento.xml   (usa las copias fieles de 00-fuentes/xsd/, requiere red
 *                                              para resolver los xs:include absolutos)
 *
 * Código de salida: 0 si todos los documentos son válidos, 1 si alguno no lo es.
 * Elige el XSD por el elemento raíz: rDE -> siRecepDE_v150.xsd; gGroupGesEve -> siRecepEvento_v150.xsd.
 */
$args = array_slice($argv, 1);
$fiel = false;
if (isset($args[0]) && $args[0] === '--fiel') {
    $fiel = true;
    array_shift($args);
}
if (!$args) {
    fwrite(STDERR, "Uso: php validar.php [--fiel] documento.xml [...]\n");
    exit(2);
}
$dir = $fiel ? realpath(__DIR__ . '/../../00-fuentes/xsd') : __DIR__;
libxml_use_internal_errors(true);
$salida = 0;
foreach ($args as $ruta) {
    $doc = new DOMDocument();
    if (!$doc->load($ruta, LIBXML_NONET)) {
        echo "$ruta: XML mal formado\n";
        foreach (libxml_get_errors() as $e) echo "   línea {$e->line}: " . trim($e->message) . "\n";
        libxml_clear_errors();
        $salida = 1;
        continue;
    }
    $raiz = $doc->documentElement->localName;
    $xsd = match ($raiz) {
        'rDE' => 'siRecepDE_v150.xsd',
        'gGroupGesEve' => 'siRecepEvento_v150.xsd',
        default => null,
    };
    if ($xsd === null) {
        echo "$ruta: raíz <$raiz> no reconocida (se esperaba rDE o gGroupGesEve)\n";
        $salida = 1;
        continue;
    }
    $ok = $doc->schemaValidate($dir . DIRECTORY_SEPARATOR . $xsd);
    if ($ok) {
        echo "$ruta: VÁLIDO contra $xsd" . ($fiel ? ' (copias fieles)' : '') . "\n";
    } else {
        echo "$ruta: INVÁLIDO contra $xsd" . ($fiel ? ' (copias fieles)' : '') . "\n";
        foreach (libxml_get_errors() as $e) echo "   línea {$e->line}: " . trim($e->message) . "\n";
        $salida = 1;
    }
    libxml_clear_errors();
}
exit($salida);
