<%inherit file="leaguenotifier:templates/inc/main.mako"/>

<div class="container">

    <div id="login-overlay" class="modal-dialog">
      <div class="modal-content">
          <div class="modal-body">
              <div class="row">
                  <div class="col-xs-6">
                      <div class="well login-well">
                          <form id="loginForm" method="POST" action="/login">
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
                              <button type="submit" value="login" name="submit" class="btn btn-success btn-block">Login</button>
                          </form>
                      </div>
                  </div>
                  <div class="col-xs-6">
                      <p class="lead">Register now</p>
                      <ul class="list-unstyled" style="line-height: 2">
                          <li><span class="fa fa-check text-success"></span> Add usernames to follow</li>
                          <li><span class="fa fa-check text-success"></span> Something more</li>
                          <li><span class="fa fa-check text-success"></span> Even more</li>
                          <li><span class="fa fa-check text-success"></span> More more more</li>
                      </ul>
                      <p><a href="./register" class="btn btn-info btn-block">Yes please, register now!</a></p>
                  </div>
              </div>
          </div>
      </div>
  </div>

</div>

<%block name="scripts">
    <script src="${request.static_url('leaguenotifier:static/js/script.js')}"></script>
</%block>
