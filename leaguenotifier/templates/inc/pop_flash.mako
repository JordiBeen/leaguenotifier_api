% for m in request.session.pop_flash():
    <div class="container feedback">
        <div class="row">
            <div class="well well-sm">
                 <p class="success"><i class="fa fa-info fa-fw"></i> ${m}</p>
            </div>
        </div>
    </div>
% endfor