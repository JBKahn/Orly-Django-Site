module.exports = function(grunt) {

    grunt.initConfig({
        concat: {
            js: {
                src: [
                    'bower_components/jquery/dist/jquery.min.js',
                    'bower_components/bootstrap/dist/js/bootstrap.min.js',
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
                    'bower_components/masonry/masonry.js'
                ],
                dest: 'static/js/requirements.dist.js'
            },
            css: {
                src: [
                    'bower_components/bootstrap/dist/css/bootstrap.min.css',
                    'bower_components/blueimp-gallery/css/blueimp-gallery.min.css',
                    'static-src-build/css/style.css'
                ],
                dest: 'static/css/style.dist.css'
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
                    // "jade/*"
                ],
                tasks: ['default']
            }
        },

        // jade: {
        //     compile: {
        //         options: {
        //             client: false,
        //             pretty: true
        //         },
        //         files: [ {
        //           cwd: "jade/",
        //           src: "*.jade",
        //           dest: "./",
        //           expand: true,
        //           ext: ".html"
        //         } ]
        //     }
        // },

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

    grunt.registerTask('default', ['sass', 'concat']);
    grunt.registerTask('dev', ['default', 'connect', 'watch']);

};
