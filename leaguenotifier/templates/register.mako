<%inherit file="leaguenotifier:templates/inc/main.mako"/>

<div class="container">

    <div id="login-overlay" class="modal-dialog">
      <div class="modal-content">
          <div class="modal-body">
              <div class="row">
                  <div class="col-xs-12">
                      <div class="well login-well">
                          <form id="loginForm" method="POST">
                              <div class="form-group">
                                  <label for="username" class="control-label">Username</label>
                                  <input type="text" class="form-control" name="username" value="" required="" title="Please enter your username" placeholder="username">
                                  <span class="help-block"></span>
                              </div>
                              <div class="form-group">
                                  <label for="password" class="control-label">Password</label>
                                  <input type="password" class="form-control" name="password" placeholder="password" value="" required="" title="Please enter your password">
                                  <span class="help-block"></span>
                              </div>
                              <div class="form-group">
                                  <label for="email" class="control-label">E-mail address</label>
                                  <input type="email" class="form-control" name="email" placeholder="email" value="" required="" title="Please enter your email">
                                  <span class="help-block"></span>
                              </div>
                              <button type="submit" value="login" name="submit" class="btn btn-success btn-block">Register</button>
                          </form>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>

</div>

<%block name="scripts">
    <script src="${request.static_url('leaguenotifier:static/js/script.js')}"></script>
</%block>
