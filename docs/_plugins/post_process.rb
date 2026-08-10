# Jekyll plugin to run post-processing scripts after build

require 'open3'

Jekyll.logger.info "Loading post_process plugin..."

Jekyll::Hooks.register :site, :post_write do |site|
  Jekyll.logger.info "Running post-processing scripts..."
  
  # Get the current working directory (web-foundations)
  cwd = File.dirname(__FILE__) + '/../..'
  
  # Run normalize-ids
  Jekyll.logger.info "Running normalize-ids..."
  stdout, stderr, status = Open3.capture3('node', 'scripts/normalize-ids.mjs', chdir: cwd)
  puts stdout unless stdout.empty?
  puts stderr unless stderr.empty?
  
  # Run mark-broken-links
  Jekyll.logger.info "Running mark-broken-links..."
  stdout, stderr, status = Open3.capture3('node', 'scripts/mark-broken-links.mjs', chdir: cwd)
  puts stdout unless stdout.empty?
  puts stderr unless stderr.empty?
  
  Jekyll.logger.info "Post-processing complete!"
end

