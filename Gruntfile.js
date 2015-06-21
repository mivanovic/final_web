module.exports = function(grunt) {

  grunt.initConfig({

    imagemin: {                          // Task
      dynamic: {                         // Another target
        options: {                       // Target options
          optimizationLevel: 3,
          svgoPlugins: [{ removeViewBox: false }]
        },
        files: [{
          expand: true,                  // Enable dynamic expansion
          cwd: 'img/',                   // Src matches are relative to this path
          src: ['*.{png,jpg,gif}'],   // Actual patterns to match
          dest: 'img/'                  // Destination path prefix
        }]
      }
    },

    watch: {
      files: ['<%= jshint.files %>'],
      tasks: ['jshint']
    },

    cssmin: {
      target: {
        files: [{
          expand: true,
          cwd: 'static/css/',
          src: ['*.css', '!*.min.css'],
          dest: 'static/css/',
          ext: '.min.css'
        }]
      }
    },

    uglify: {
      my_target: {
        files: {
          'js/output.min.js': [
                                'static/js/jquery-migrate-1.2.1.js',
                                'static/js/jquery.ui.totop.js'
                                ]
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-imagemin');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-uglify');

  grunt.registerTask('default', ['imagemin', 'cssmin', 'uglify']);

};