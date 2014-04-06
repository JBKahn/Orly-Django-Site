module.exports = function(grunt) {

    grunt.initConfig({
        concat: {
            js: {
                src: [
                    'bower_components/jquery/dist/jquery.min.js',
                    'bower_components/bootstrap/dist/js/bootstrap.min.js',
                    'bower_components/bootstrap-datepicker/js/bootstrap-datepicker.js',
                    'bower_components/blueimp-gallery/js/jquery.blueimp-gallery.min.js',
                    'bower_components/get-style-property/get-style-property.js', // Masonry requirement
                    'bower_components/get-size/get-size.js', // Masonry requirement
                    'bower_components/eventie/eventie.js', // Masonry requirement
                    'bower_components/doc-ready/doc-ready.js', // Masonry requirement
                    'bower_components/eventEmitter/EventEmitter.min.js', // Masonry requirement
                    'bower_components/jquery-bridget/jquery.bridget.js', // Masonry requirement
                    'bower_components/matches-selector/matches-selector.js', // Masonry requirement
                    'bower_components/outlayer/item.js', // Masonry requirement
                    'bower_components/outlayer/outlayer.js', // Masonry requirement
                    'bower_components/masonry/masonry.js',
                    'static-src/js/app.js'
                ],
                dest: 'static/js/requirements.dist.js'
            },
            css: {
                src: [
                    'bower_components/bootstrap-datepicker/css/datepicker.css',
                    'bower_components/bootstrap/dist/css/bootstrap.min.css',
                    'bower_components/blueimp-gallery/css/blueimp-gallery.min.css',
                    'bower_components/font-awesome/css/font-awesome.min.css',
                    'static-src-build/css/style.css'
                ],
                dest: 'static/css/style.dist.css'
            }
        },

        copy: {
            main: {
                files: [
                    // includes files within path
                    {expand: true, flatten: true, src: ['bower_components/font-awesome/fonts/*'], dest: 'static/fonts/', filter: 'isFile'},
                ]
            }
        },

        connect: {
            server: {
                options: {
                    port: "9001"
                }
            }
        },

        watch: {
            dev: {
                files: [
                    "static-src/sass/*",
                    "static-src/js/*",
                    "static-src/jade/*"
                ],
                tasks: ['default']
            }
        },

        jade: {
            compile: {
                options: {
                    client: false,
                    pretty: true
                },
                files: [ {
                  cwd: "static-src/jade/",
                  src: "base.jade",
                  dest: "templates/",
                  expand: true,
                  ext: ".html"
                } , {
                  cwd: "static-src/jade/",
                  src: "gallery.jade",
                  dest: "templates/",
                  expand: true,
                  ext: ".html"
                } , {
                  cwd: "static-src/jade/",
                  src: "artist.jade",
                  dest: "artist/templates/",
                  expand: true,
                  ext: ".html"
                } , {
                  cwd: "static-src/jade/",
                  src: "community.jade",
                  dest: "community/templates/",
                  expand: true,
                  ext: ".html"
                } , {
                  cwd: "static-src/jade/",
                  src: "contact.jade",
                  dest: "contact/templates/",
                  expand: true,
                  ext: ".html"
                } , {
                  cwd: "static-src/jade/",
                  src: "home.jade",
                  dest: "home/templates/",
                  expand: true,
                  ext: ".html"
                } , {
                  cwd: "static-src/jade/",
                  src: "portfolio.jade",
                  dest: "portfolio/templates/",
                  expand: true,
                  ext: ".html"
                } , {
                  cwd: "static-src/jade/",
                  src: "special_effects.jade",
                  dest: "special_effects/templates/",
                  expand: true,
                  ext: ".html"
                } , {
                  cwd: "static-src/jade/",
                  src: "services.jade",
                  dest: "services/templates/",
                  expand: true,
                  ext: ".html"
                } , {
                  cwd: "static-src/jade/",
                  src: "reviews.jade",
                  dest: "reviews/templates/",
                  expand: true,
                  ext: ".html"
                }]
            }
        },

        sass: {
          dist: {
            files: {
              "static-src-build/css/style.css": 'static-src/sass/style.scss',
            }
          }
        },
    });

    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-connect');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-jade');
    grunt.loadNpmTasks('grunt-contrib-copy');

    grunt.registerTask('default', ['sass', 'concat', 'copy', 'jade']);
    grunt.registerTask('dev', ['default', 'connect', 'watch']);

};
