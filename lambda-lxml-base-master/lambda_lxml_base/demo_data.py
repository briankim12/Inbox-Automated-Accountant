HTML = """
<!DOCTYPE html>
<html style="overflow-x: hidden;" lang="">
<head>
    <meta charset="utf-8">
    <title></title>
    <meta name="description" content=""/>
    <meta name="keywords" content=""/>
    <meta name="robots" content=""/>
    <link href='http://fonts.googleapis.com/css?family=Raleway:400,700' rel='stylesheet' type='text/css'/>
    <link href='http://fonts.googleapis.com/css?family=Raleway:900&text=ACGELPRONSY' rel='stylesheet' type='text/css'/>
    <link rel='stylesheet' type='text/css' href="/static/css/bootstrap.min.css"/>
    <link href="/static/css/font-awesome.css" rel="stylesheet">
    <link rel='stylesheet' type='text/css' href="/static/css/bootstrap.lightbox.css"/>
    <link rel='stylesheet' type='text/css' href="/static/css/plexseo-home.css"/>

    <script src="/static/js/jquery.js"></script>

    <script src="/static/js/jquery.form.js"></script>
    <script src="http://ajax.aspnetcdn.com/ajax/jquery.validate/1.11.1/jquery.validate.js"></script>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/gsap/latest/TweenMax.min.js"></script>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/gsap/latest/plugins/ScrollToPlugin.min.js"></script>
    <script type="text/javascript" src="/static/js/jstz.min.js"></script>

</head>
<body>



<div class="wrapper-tablescape">
    <div class="container">
        <div class="row">

            <div class="col-md-12">
                <div class="login pull-right">
                    <a href="/login/" class="btn btn-success"><i class="fa fa-key"></i>&nbsp;Log in</a>
                </div>


                <div class="desk-stuff">
                    <img class="north" src="/static/images/table-objects-top.png"/>
                    <img class="northwest" src="/static/images/table-objects-NW.png"/>
                    <img class="northeast" src="/static/images/table-objects-NE.png"/>
                    <img class="southwest" src="/static/images/table-objects-SW.png"/>
                    <img class="southeast" src="/static/images/table-objects-SE.png"/>
                    <img id="pencil" class="pencil" src="/static/images/yellow-pencil.png"/>
                    <img id="pencil-alt" class="pencil" src="/static/images/yellow-pencil-alt.png" style="display:none;"/>

                    <div class="desk-title">
                        <img class="desk-logo" src="/static/images/table-objects-logo.png"/>

                        <div class="desk-text clearfix">
                            <div class="its-seo">
                                <span class="its script">it's</span>
                                <span class="huge">SEO</span>

                                <div class="sidebar">
                                    <span style="font-size:187.5%;line-height:1;">for people</span> <br/>
                                    <span class="script">with</span><br/>
										<span style="font-size:287.5%;font-weight:700;line-height:1;">better<br/>
										things</span><br/>
                                    <span class="script">to do</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- .desk-title -->

                </div>
                <!-- .desk-stuff -->

            </div>
            <!-- .col-md-12 -->

        </div>
        <!-- .row -->
    </div>
    <!-- .container -->
</div>
<!-- .wrapper-tablescape -->

<div class="wrapper-cta top-cta">
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <h2>Get the metrics you need and the knowledge to improve them with <strong
                        id="plexseo-name">Plexseo</strong>.</h2>
            </div>
        </div>
        <!-- .row -->
        <div id="formdiv" class="row formrow">
            <form id="signupform" class="signupform" method="post" action="/signup/">
                <input type='hidden' name='csrfmiddlewaretoken' value='NoprYQXtFxr9JfgsMm9FyFEJaZa33RAN' />
                <div class="col-md-8">
                    <input type="text" class="form-control" id="email" name="email" placeholder="Your e-mail address"/>
                </div>
                <div class="col-md-4">
                    <img class="cta-burst" src="/static/images/cta-burst.png" alt="" style="display:none;"/>
                    <button id="pencil-button" class="btn btn-primary btn-block">Try it out for free <i
                            class="fa fa-arrow-right"></i></button>
                </div>
            </form>
        </div>

        <div id="thanksdiv" class="thanksrow alert alert-success" style="display:none;">
            Thank you for signing up! Please check your email for activation instructions.
        </div>



        <div class="row">
            <div class="col-md-12">
                <p class="tinytext">No credit card required. You can use the Free plan for as long as you like.
                    Seriously, go nuts.</p>
            </div>
        </div>
        <!-- .row -->
    </div>
</div>
<!-- .wrapper-cta -->

<div class="wrapper-targets">
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <div class="dartboard-group">

                    <img src="/static/images/goals-arrow-shadow-start.png" id="arrow-shadow-start" class="arrow-shadow-start"
                         alt=""/>
                    <img src="/static/images/goals-arrow-shadow-end.png" id="arrow-shadow-end" class="arrow-shadow-end" alt=""/>
                    <img src="/static/images/goals-arrow-start.png" id="arrow-start" class="arrow-start" alt=""/>
                    <img src="/static/images/goals-arrow-mid.png" id="arrow-mid" class="arrow-mid" alt=""/>
                    <img src="/static/images/goals-arrow-end.png" id="arrow-end" class="arrow-end" alt=""/>
                    <img src="/static/images/goals-dartboard.png" class="dartboard" alt=""/>
                </div>
            </div>
            <div class="col-md-6 target-details">
                <h2>Plexseo makes it easy to hit your traffic targets.</h2>

                <p>Plexseo's crawler scans all your sites and offers simple, effective tips for fixing the issues it
                    finds. </p>

                <div class="thumbnails" data-toggle="lightbox">
                    <div class="col-md-6 col-xs-6">
                        <a href="http://cooperbold.com/clients/plexseo/parallax//static/images/goals-dartboard.png"
                           data-title="test" class="thumbnail">
                            <img src="http://placehold.it/230x130" alt=""/>
                        </a>
                    </div>
                    <div class="col-md-6 col-xs-6">
                        <a href="#" class="thumbnail">
                            <img src="http://placehold.it/230x130" alt=""/>
                        </a>
                    </div>
                    <div class="col-md-6 col-xs-6">
                        <a href="#" class="thumbnail">
                            <img src="http://placehold.it/230x130" alt=""/>
                        </a>
                    </div>
                    <div class="col-md-6 col-xs-6">
                        <a href="#" class="thumbnail">
                            <img src="http://placehold.it/230x130" alt=""/>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        <!-- .row -->
    </div>
</div>
<!-- .wrapper-targets -->

<div class="wrapper-whitelabel">
    <div class="container">
        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-10">
                <h2>Impress your clients with our sexy, seamless white-labeled client lounge.</h2>

                <p>Plexseo makes you look good. Add your logo and branding elements, link it to your domain,
                    set up your users, and watch the praise roll in. Nobody has to know the secret in your sauce.</p>
                <img id="wand" class="wand" src="/static/images/whitelabel-wand.png"/>
                <img class="whitelabel lame" src="/static/images/whitelabel-lame.png" alt=""/>
                <img class="whitelabel awesome" src="/static/images/whitelabel-awesome.png" alt=""/>
                <img class="whitelabel-stars left" src="/static/images/whitelabel-stars-left.png" alt=""/>
                <img class="whitelabel-stars right" src="/static/images/whitelabel-stars-right.png" alt=""/>
            </div>
            <div class="col-md-1"></div>
        </div>
    </div>
</div>

<div class="wrapper-prices" id="pricing">
    <div class="container">
        <div class="row price-details">
            <div class="col-md-12">
                <h2>Prices so reasonable, you'll be pleasantly surprised.</h2>

                <p>Sign up for free. Upgrade, downgrade, or cancel anytime. No credit card required.</p>
            </div>
        </div>
        <!-- .row -->
        <div class="row">
            <div class="col-md-12">
                <table class="price-table">
                    <tr>
                        <td>
                            <div class="price-group queen">
                                <div class="price-icon">
                                    <img src="/static/images/pricing-queen.png" alt=""/>
                                </div>
                                <div class="price-sheet-edge"></div>
                                <div class="price-sheet" style="height:460px;">
                                    <div class="price-sheet-header clearfix">
                                        <span class="price-title pull-left">Agency</span>
                                        <span class="price-amt pull-right"><sup>$</sup>99</span>
                                    </div>
                                    <div class="price-sheet-subhead">
                                        <strong>Tools for your team</strong><br/>
                                        <small><em>Cutting-edge SEO services for all your clients or projects</em>
                                        </small>
                                    </div>
                                    <ul class="price-features">
                                        <li><strong>25</strong> websites!</li>
                                        <li><strong>1,000</strong> page crawls
                                            <small class="nobr"><em>per site</em></small>
                                        </li>
                                        <li><strong>350</strong> keywords</li>
                                        <li><strong>Priority support</strong></li>
                                        <li>SEO issues report</li>
                                        <li>Uptime monitor</li>
                                        <li>White-labeled client dashboard</li>
                                        <li>Unlimited user accounts</li>
                                    </ul>
                                </div>
                            </div>
                        </td>

                        <td>
                            <div class="price-group knight">
                                <div class="price-icon">
                                    <img src="/static/images/pricing-knight.png" alt=""/>
                                </div>
                                <div class="price-sheet-edge"></div>
                                <div class="price-sheet">
                                    <div class="price-sheet-header clearfix">
                                        <span class="price-title pull-left">Pro</span>
                                        <span class="price-amt pull-right"><sup>$</sup>29</span>
                                    </div>
                                    <div class="price-sheet-subhead">
                                        <strong>Our most popular plan!</strong><br/>
                                        <small><em>SEO for small teams<br/>& busy professionals</em></small>
                                    </div>
                                    <ul class="price-features">
                                        <li><strong>Five</strong> websites<br/>
                                            <small><em>Add more sites for <span class="nobr">$5 each</span></em></small>
                                        </li>
                                        <li><strong>1,000</strong> page crawls
                                            <small class="nobr"><em>per site</em></small>
                                        </li>
                                        <li><strong>50</strong> keywords</li>
                                        <li>SEO issues report</li>
                                        <li>Uptime monitor</li>
                                        <li>White-labeled client dashboard</li>
                                        <li>Unlimited user accounts</li>
                                    </ul>
                                </div>
                            </div>
                        </td>

                        <td>
                            <div class="price-group pawn">
                                <div class="price-icon">
                                    <img src="/static/images/pricing-pawn.png" alt=""/>
                                </div>
                                <div class="price-sheet-edge"></div>
                                <div class="price-sheet">
                                    <div class="price-sheet-header clearfix">
                                        <span class="price-title pull-left">Solo</span>
                                        <span class="price-free pull-right"><span
                                                class="script">Free</span>Forever</span>
                                    </div>
                                    <div class="price-sheet-subhead">
                                        <strong>Build a better site</strong><br/>
                                        <small><em>Powerful SEO tools help you optimize your website</em></small>
                                    </div>
                                    <ul class="price-features">
                                        <li><strong>One</strong> website</li>
                                        <li><strong>100</strong> page crawls</li>
                                        <li><strong>5</strong> keywords</li>
                                        <li><strong>Priority support</strong></li>
                                        <li>SEO issues report</li>
                                        <li>Uptime monitor</li>
                                        <li>One user account</li>
                                    </ul>
                                </div>
                            </div>
                            <!-- .pawn -->
                        </td>

                    </tr>
                </table>
            </div>


        </div>
    </div>
</div>

<div class="wrapper-cta bottom-cta">
    <div class="container">
        <div id="formdiv" class="row formrow">
            <form id="signupform" class="signupform" method="post" action="plx-signup.php">
                <input type='hidden' name='csrfmiddlewaretoken' value='NoprYQXtFxr9JfgsMm9FyFEJaZa33RAN' />
                <div class="col-md-8">
                    <input type="text" class="form-control" id="email" name="email" placeholder="Your e-mail address"/>
                </div>
                <div class="col-md-4">
                    <img class="cta-burst" src="/static/images/cta-burst.png" alt="" style="display:none;"/>
                    <button id="pencil-button" class="btn btn-primary btn-block">Try it out for free <i
                            class="fa fa-arrow-right"></i></button>
                </div>
            </form>
        </div>

        <div id="thanksdiv" class="thanksrow alert alert-success" style="display:none;">
            Thank you for signing up! Please check your email for activation instructions.
        </div>


    </div>
</div>
<!-- .wrapper-cta -->

<div class="wrapper-blog">
    <div class="container">
        <div class="row">
            <div class="col-md-4">
                <img src="/static/images/blog-clock-and-coffee.png" alt="" class="blog-image"/>
            </div>
            <div class="col-md-8">
                <h2><a href="#">Do alt tags really matter?</a></h2>
                <ul class="post-info">
                    <li class="time">
                        <i class="fa fa-clock-o"></i>&nbsp;February 16, 2014
                    </li>
                    <li class="category">
                        <i class="fa fa-folder-open"></i>&nbsp;<a href="#">SEO Tactics</a>
                    </li>
                </ul>
                <div class="post-content">
                    <p>Conveniently actualize installed base interfaces without low-risk high-yield networks.
                        Compellingly cultivate innovative technology via standards compliant niche markets. </p>

                    <p>Monotonectally evisculate standardized process improvements without front-end mindshare. </p>

                    <p class="readmore"><a href="#">Read more <i class="fa fa-arrow-right"></i></a></p>
                </div>
            </div>
        </div>
        <!-- .row -->
    </div>
</div>
<!-- .wrapper-cta -->

<div class="wrapper-footer">
    <div class="container">
        <div class="row">
            <p class="pull-left">
                <small>&copy;<?php echo date("Y"); ?> Plexseo, LLC. All rights reserved.</small>
            </p>
            <ul class="social pull-right">
                <li>
                    <a href="http://facebook.com/pages/plexseo" target="_blank" class="social-facebook"><i
                            class="fa fa-facebook-square"></i></a>
                </li>
                <li>
                    <a href="http://twitter.com/plexseo" target="_blank" class="social-twitter"><i
                            class="fa fa-twitter-square"></i></a>
                </li>
                <li>
                    <a href="#" target="_blank" class="social-gplus"><i class="fa fa-google-plus-square"></i></a>
                </li>
            </ul>

        </div>
        <!-- .row -->
    </div>
</div>
<!-- .wrapper-cta -->




</body>
</html>
 """