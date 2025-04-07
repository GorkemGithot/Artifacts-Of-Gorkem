<?php
echo !defined("GUVENLIK") ? die("Vaoww! Bu ne cesaret?") : null;
?>
<title>Varyant Seçenekleri | <?= htmlspecialchars($ayar['site_baslik']) ?></title>
<?php
// Gerekli tanımlar
$varyant_id = isset($_GET['varyant_id']) ? intval($_GET['varyant_id']) : 0;
$page = isset($_GET['page']) ? intval($_GET['page']) : 1;
$page = $page > 0 ? $page : 1;

// Varyant verisi çek
$varyantQuery = $db->prepare("SELECT * FROM varyant WHERE id = :id");
$varyantQuery->bindParam(':id', $varyant_id, PDO::PARAM_INT);
$varyantQuery->execute();
$varyant = $varyantQuery->fetch(PDO::FETCH_ASSOC);

// Varyant yoksa yönlendir
if (!$varyant) {
    header("Location: pages.php?sayfa=urunler");
    exit;
}

// Varyanta ait özellikler
$limit = 500;
$offset = ($page - 1) * $limit;

$ozellikQuery = $db->prepare("SELECT * FROM varyant_oz WHERE varyant_id = :id ORDER BY sira ASC LIMIT :offset, :limit");
$ozellikQuery->bindParam(':id', $varyant_id, PDO::PARAM_INT);
$ozellikQuery->bindParam(':offset', $offset, PDO::PARAM_INT);
$ozellikQuery->bindParam(':limit', $limit, PDO::PARAM_INT);
$ozellikQuery->execute();
$ozellikler = $ozellikQuery->fetchAll(PDO::FETCH_ASSOC);

// Toplam veri sayısı
$countQuery = $db->prepare("SELECT COUNT(*) FROM varyant_oz WHERE varyant_id = :id");
$countQuery->bindParam(':id', $varyant_id, PDO::PARAM_INT);
$countQuery->execute();
$totalCount = $countQuery->fetchColumn();

$pageCount = ceil($totalCount / $limit);
$page = $page > $pageCount ? 1 : $page;

// Ürüne geri dönmek için ürün ID
$urun_id = intval($varyant['urun_id']);
?>

<div class="row page-titles">
    <div class="col-md-5 align-self-center">
        <h4 class="text-themecolor"><i class="mdi mdi-debug-step-into"></i> Varyant Seçenekleri</h4>
    </div>
    <div class="col-md-7 align-self-center text-right">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="javascript:void(0)">Yönetim Paneli</a></li>
            <li class="breadcrumb-item"><a href="javascript:void(0)">Varyant Ayarları</a></li>
            <li class="breadcrumb-item active">Varyant Seçenekleri</li>
        </ol>
    </div>
</div>

<div class="row">
    <div class="col-md-12 text-left">
        <a href="pages.php?sayfa=varyantlar&urun_id=<?= $urun_id ?>" class="btn btn-dark m-b-15"><i class="fa fa-arrow-left"></i> Geri Dön</a>
        <a href="pages.php?sayfa=varyantozellikekle&varyant_id=<?= $varyant_id ?>" class="btn btn-info m-b-15"><i class="fa fa-plus-circle"></i> Yeni Seçenek Ekle</a>
    </div>

    <div class="col-12">
        <div class="card">
            <div class="card-body text-white" style="background: linear-gradient(to right, #4568dc, #b06ab3);">
                <h3 class="card-title">Varyant Adı: <?= htmlspecialchars($varyant['baslik']) ?></h3>
            </div>
        </div>

        <div class="card">
            <div class="card-body bg-secondary">
                <h3 class="card-title m-b-25">Varyant Seçenekleri</h3>
                <h6 class="card-subtitle">Seçili varyantınıza özellikler ekleyebilirsiniz.</h6>
            </div>
        </div>

        <div class="card" style="margin-bottom: 0 !important;">
            <div class="card-body" style="padding: 15px !important;">
                <?php if (count($ozellikler) > 0): ?>
                <div class="table-responsive">
                    <table class="table table-bordered table-striped" style="font-family: 'Open Sans', Arial;">
                        <thead>
                            <tr>
                                <th width="1%">SIRA</th>
                                <th>VARYANT ÖZELLİĞİ</th>
                                <th width="180" class="text-center">#</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach ($ozellikler as $ozellik): ?>
                            <tr>
                                <td><span class="btn btn-sm btn-dark text-white"><?= $ozellik['sira'] ?></span></td>
                                <td><?= htmlspecialchars($ozellik['ozellik']) ?></td>
                                <td class="text-center">
                                    <a href="pages.php?sayfa=varyantozellik&ozellik_id=<?= $ozellik['id'] ?>" class="btn btn-sm btn-info"><i class="fa fa-pencil"></i> Düzenle</a>
                                    <a onclick="deletebutton(<?= $ozellik['id'] ?>, <?= $ozellik['varyant_id'] ?>)" class="btn btn-sm btn-danger"><i class="fa fa-times"></i> Sil</a>
                                </td>
                            </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                </div>
                <?php else: ?>
                <div class="alert alert-info">Henüz bu varyanta seçenek eklenmemiş!</div>
                <?php endif; ?>
            </div>
        </div>
    </div>
</div>

<script type="text/javascript">
function deletebutton(ozellikid, tabloid) {
    swal({
        title: "Silmek İstediğinize Emin Misiniz?",
        text: "Seçtiğiniz içerik kalıcı olarak silinecektir",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "Sil",
        cancelButtonText: "İptal",
        closeOnConfirm: false,
        closeOnCancel: false
    }, function(isConfirm){
        if (isConfirm) {
            window.location.href = "support/post/delete/varyant-ozellik-sil.php?varyant=success&id=" + ozellikid + "&varyant_id=" + tabloid;
        } else {
            swal("İptal Edildi", "Seçtiğiniz içerik silinmemiştir", "error");
        }
    });
}
</script>

<?php if (isset($_GET['status'])):
    $status = $_GET['status'];
    $messages = [
        'success' => ['İşlem Başarılı', 'İşleminiz başarıyla gerçekleşmiştir', 'success'],
        'warning' => ['Başarısız!', 'İşlem sırasında hata oluştu', 'warning'],
        'nocheck' => ['Sorun Var!', 'Hiç seçim yapılmamış!', 'warning'],
    ];
    if (isset($messages[$status])):
?>
    <body onload="sweetAlert('<?= $messages[$status][0] ?>', '<?= $messages[$status][1] ?>', '<?= $messages[$status][2] ?>');">
    </body>
    <meta http-equiv="refresh" content="1; URL=pages.php?sayfa=varyantozellikleri&varyant_id=<?= $varyant_id ?>">
<?php endif; endif; ?>
